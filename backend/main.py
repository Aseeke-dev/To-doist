from fastapi import FastAPI, Depends
from app.api.routes.items import router as items_router
from app.core.model import Base
from app.core.db import engine
from app.api.routes.user import router as user_router
from app.api.routes.login import router as login_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do List API", version="1.0.0")

app.include_router(items_router)
app.include_router(user_router)
app.include_router(login_router)