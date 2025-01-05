from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")

def get_items()->dict:
    return {"message": "Users work"}