from pydantic import BaseModel,EmailStr # basemodel is to converts json data to python types validates automatically
class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserOut(UserCreate):  ## this defines what data to return back to users
    id: int

    #name:str
    #email:EmailStr
    class Config:
        orm_mode = True
