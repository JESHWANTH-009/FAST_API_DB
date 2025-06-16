from datetime import datetime,timedelta #required to calculate token expirey
from jose import jwt,JWTError  ##jwt--encode/decode
from passlib.context import CryptContext ## password hashing verification
from fastapi.security import OAuth2PasswordBearer #Bearer token authentication

#from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session  # like a conncetion 
import models,database
import os
from dotenv import load_dotenv #load .env config
import os
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")
load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")  ##secret to signn tokens
ALGORITHM=os.getenv("ALGORITHM")##HS256 is mostly used 
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


##password hashing

pwd_context=CryptContext(schemes=['bcrypt'],deprecated="auto")  ##sets 'bcrypt' as hashing algorithm
def get_password_hash(password):
    return pwd_context.hash(password)  ##hasing password before storing it in db

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)  ##check plain password matches hashed in db

                  ##now generatiing TOKEN


def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})      ##adding expiration to token
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.SessionLocal)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = db.query(models.User).filter(models.User.username == username).first()
        if user is None:
            raise credentials_exception
        return user
    except JWTError:
        raise credentials_exception