from fastapi import FastAPI
from database import engine
import models
from routers import user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)
