from datetime import datatime,timedelta #required to calculate token expirey
from jose import jwt,JWTError  ##jwt--encode/decode
from passlib.context import CryptContext ## password hashing verification
from fastapi.security import OAuth2PasswordBearer #Bearer token authentication

from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session  # like a conncetion 
import models,database
import os
from dotenv import load_dotenv #load .env config
import os

load_dotenv()

SECRET_KEY=os.getenv("SECRET KEY")  ##secret to signn tokens
ALGORITHM=os.getenv("ALGORITHM")##HS256 is mostly used 
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


##password hashing

pwd_context=CryptContext(schemes=['bcrypt'],deprecated="auto")
def get_password_hash(password):
    return pwd_context.hash(password)  ##hasing password before storing it in db
