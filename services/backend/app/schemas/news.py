from pydantic.main import BaseModel


class NewsBase(BaseModel):
    pass


class NewsCreate(NewsBase):
    title: str
    description: str


class NewsUpdate(NewsBase):
    title: str
    description: str
