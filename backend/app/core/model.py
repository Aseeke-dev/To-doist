from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

Base = declarative_base()

class ToDoItem(Base):
    __tablename__ = "todo_items"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    status = Column(String, nullable=False, default="pending")
    priority = Column(String, nullable=False, default="medium")
    created_at = Column(String, default=datetime.utcnow, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="todo_items")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    created_at = Column(String, default=datetime.utcnow, index=True, nullable=False)
    todo_items = relationship("ToDoItem", back_populates="user")