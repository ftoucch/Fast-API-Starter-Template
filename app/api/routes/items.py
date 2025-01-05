from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")

def get_items()->dict:
    return {"message": "Items works"}