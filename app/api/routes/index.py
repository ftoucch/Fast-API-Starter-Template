from fastapi import APIRouter
from sqlmodel import Session

router = APIRouter(prefix="", tags=["index"])


@router.get("/")
def get_items()->dict:
    return {"message": "welcome to text to speech api"}