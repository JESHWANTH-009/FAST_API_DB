from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserOut(BaseModel): #this is return what output can user see 
    id:int
    username:str
    email:EmailStr
    class Config:
        orm_mode=True

class Token(BaseModel):## for token genration JWT token responses after successfull login
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
