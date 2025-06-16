from fastapi import FastAPI
from database import Base, engine
from routers import user, item

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(item.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI with MySQL & Auth"}
