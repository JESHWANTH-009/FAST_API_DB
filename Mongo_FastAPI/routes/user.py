from fastapi import APIRouter,HTTPException
from database import user_collection
from models import User,Userout
from bson import ObjectId, errors as bson_errors
 
router=APIRouter()

def user_serializer(user) -> dict:
    return{"id":str(user["_id"]),  # as id is primary key we store in mongodb as "_id"
           "name":user["name"],
           "email":user["email"]}

@router.post("/workers", response_model=Userout)
async def create_user(user: User):
    result = await user_collection.insert_one(user.dict())
    new_user = await user_collection.find_one({"_id": result.inserted_id})
    return user_serializer(new_user)

@router.get("/workers", response_model=list[Userout])
async def get_users():
    users = []
    async for user in user_collection.find():
        users.append(user_serializer(user))
    return users

@router.get("/workers/{id}", response_model=Userout)
async def get_user(id: str):
    try:
        obj_id = ObjectId(id)
    except bson_errors.InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID format")
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_serializer(user)
    raise HTTPException(status_code=404, detail="User not found")