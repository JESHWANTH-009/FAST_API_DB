from pydantic import BaseModel,EmailStr
from typing import Optional

class User(BaseModel):
    name:str
    email:EmailStr

class Userout(User):
    id:Optional[str]
    