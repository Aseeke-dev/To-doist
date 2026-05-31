from fastapi import APIRouter, HTTPException, Depends
from app.core.schema import ToDoSchema
from app.core.db import get_db
from sqlalchemy.orm import Session
from app.core.model import ToDoItem as item_model
from app.core.security import get_current_user

router = APIRouter(prefix="/api", tags=["items"], dependencies=[Depends(get_current_user)])

@router.get("/items")
async def get_items(db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user)):
    items = db.query(item_model).filter(item_model.user_id == current_user_id).all()
    return items

@router.post("/items")
async def create_item(item: ToDoSchema, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user)):
    new_item = item_model(**item.model_dump(), user_id=current_user_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/items/{item_id}")
async def get_item(item_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user)):
    item = db.query(item_model).filter(item_model.id == item_id, item_model.user_id == current_user_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: ToDoSchema, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user)):
    existing_item = db.query(item_model).filter(item_model.id == item_id, item_model.user_id == current_user_id).first()
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.model_dump().items():
        setattr(existing_item, key, value)
        db.commit()
        db.refresh(existing_item)
    return existing_item

@router.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user)):
    item = db.query(item_model).filter(item_model.id == item_id, item_model.user_id == current_user_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"detail": "Item deleted successfully"}