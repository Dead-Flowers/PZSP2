from os import error
from pydantic.typing import resolve_annotations
import requests
from typing import Dict, Optional
from urllib.parse import urljoin
from io import BufferedReader
import re


def sanitize_field_name(field_name: str) -> str:
    alphanumerical_name = re.sub(
        r"[^a-z0-9]", " ", field_name.lower().replace("%", "percent")
    )
    non_empty_words = filter(None, alphanumerical_name.split(" "))
    sanitized_name = "_".join(non_empty_words)
    return sanitized_name


def sanitize_dict_keys(dict: dict) -> dict:
    return {sanitize_field_name(key): value for key, value in dict.items()}


class BowelAnalysisStatistics:
    @classmethod
    def from_dict(cls, statistics: dict) -> "BowelAnalysisStatistics":
        sanitized_statistics = sanitize_dict_keys(statistics)
        return BowelAnalysisStatistics(**sanitized_statistics)

    def __init__(self, basic_informations: dict, main_results: dict, plots: dict):
        self._basic_informations = sanitize_dict_keys(basic_informations)
        self._main_results = sanitize_dict_keys(main_results)
        self._plots = plots

    @property
    def basic_informations(self) -> dict:
        return self._basic_informations

    @property
    def main_results(self) -> dict:
        return self._main_results

    @property
    def plots(self) -> dict:
        return self._plots

    def as_dict(self):
        return dict(
            basic_informations=self.basic_informations,
            main_results=self.main_results,
            plots=self.plots,
        )


class BowelAnalysisResult:
    def __init__(
        self, result: int, frames: list, statistics: dict, error: Optional[str]
    ):
        self._result = result
        self._frames = frames
        self._statistics = statistics
        self._cached_statistics_obj = None
        self._error = error

    @property
    def is_valid(self) -> bool:
        return self._result == 200

    @property
    def error(self) -> str:
        return self._error

    @property
    def frames(self) -> list:
        return self._frames

    @property
    def raw_statistics(self) -> dict:
        return self._statistics

    @property
    def statistics(self) -> BowelAnalysisStatistics:
        if not self._cached_statistics_obj:
            self._cached_statistics_obj = BowelAnalysisStatistics.from_dict(
                self._statistics
            )
        return self._cached_statistics_obj

    def as_dict(self) -> dict:
        return dict(
            error=self.error,
            result=self._result,
            frames=self.frames,
            statistics=self.statistics.as_dict(),
        )


class BowelAnalysisService:
    def __init__(self, base_url: str):
        self._base_url = base_url

    @property
    def base_url(self) -> str:
        return self._base_url

    def combine_url(self, url_fragment: str) -> str:
        return urljoin(self.base_url, url_fragment)

    def upload_file(self, file_reader: BufferedReader):
        response = requests.post(
            self.combine_url("/backend/upload"), files=dict(file=file_reader)
        )
        response.raise_for_status()

    def get_status(self) -> BowelAnalysisResult:
        response = requests.get(self.combine_url("/backend/inference"))
        response.raise_for_status()
        body = response.json()
        return BowelAnalysisResult(**body)
