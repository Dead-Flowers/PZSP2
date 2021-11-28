from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Body, Depends, HTTPException, File, UploadFile

router = APIRouter()


@router.post("/upload")
def perform_analysis(file: UploadFile = File(...)):
    return {"filename": file.filename}
