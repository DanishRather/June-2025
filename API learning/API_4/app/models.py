# /app/models.py
from pydantic import BaseModel

# Pydantic models for input and output validation
class ApiDataCreate(BaseModel):
    name: str
    age: int

class ApiDataResponse(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        orm_mode = True
