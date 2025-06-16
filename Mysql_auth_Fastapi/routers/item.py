from fastapi import APIRouter, Depends
from auth import get_current_user

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/protected")
def get_protected_data(current_user = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}!"}
