from pydantic import BaseModel, EmailStr

class ToDoSchema(BaseModel):
    title: str
    description: str = None
    status: str
    priority: str

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
