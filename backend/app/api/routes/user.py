from fastapi import APIRouter, HTTPException, Depends
from app.core.schema import UserSchema
from app.core.db import get_db
from sqlalchemy.orm import Session
from app.core.model import User as user_model
from app.core.security import hash_password

router = APIRouter(prefix="/api", tags=["users"])

@router.post("/users")
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    existing_user = db.query(user_model).filter((user_model.username == user.username) | (user_model.email == user.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    user.password = hash_password(user.password)
    new_user = user_model(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user