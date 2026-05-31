from fastapi import APIRouter, HTTPException, Depends
from app.core.security import verify_password, create_access_token
from app.core.db import get_db
from sqlalchemy.orm import Session
from app.core.model import User as user_model
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix='/login', tags=['login'])

@router.post("/")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(user_model).filter(user_model.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    access_token = create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}