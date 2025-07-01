# app/main.py
from fastapi import FastAPI
from . import models, database
from .routes import router

app = FastAPI()
app.include_router(router)

# Comment this out if table already exists:
# models.Base.metadata.create_all(bind=database.engine)
