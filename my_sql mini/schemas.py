from pydantic import BaseModel # basemodel is to converts json data to python types validates automatically
class UserCreate(BaseModel):
    name: str
    email: str

class UserOut(UserCreate):
    id: int
    class Config:
        orm_mode = True
