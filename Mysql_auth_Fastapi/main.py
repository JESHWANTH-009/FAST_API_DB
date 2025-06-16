from fastapi import FastAPI
from database import engine, Base

# Import models so they are registered with SQLAlchemy!
import models

app = FastAPI()

# This line creates tables for all imported models
Base.metadata.create_all(bind=engine)