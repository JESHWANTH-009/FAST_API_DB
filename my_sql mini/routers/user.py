from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal() #create session with db  ###session is  temrary db connection bridge bw python code and db
    try:
        yield db #yeild provides session to db
    finally:
        db.close()

@router.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email)
    """conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Check if user with email already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (user.email,))
    existing = cursor.fetchone()
    if existing:
        conn.close()
        raise HTTPException(status_code=400, detail="Email already registered")

    # Insert user
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (user.name, user.email)
    )
    conn.commit()
    user_id = cursor.lastrowid

    # Fetch the newly created user
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    new_user = cursor.fetchone()

    cursor.close()
    conn.close()

    return new_user
    """
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # reloads object from db,so it includes fields like id
    return db_user

@router.get("/users/", response_model=list[schemas.UserOut])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
