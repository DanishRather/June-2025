# app/schemas.py
from pydantic import BaseModel

class ApiDataBase(BaseModel):
    name: str
    age: int

class ApiDataCreate(ApiDataBase):
    pass

class ApiData(ApiDataBase):
    id: int

    class Config:
        from_attributes = True  # for Pydantic v2 compatibility




# # app/schemas.py
# from pydantic import BaseModel

# class ItemBase(BaseModel):
#     name: str
#     description: str

# class ItemCreate(ItemBase):
#     pass

# class Item(ItemBase):
#     id: int

#     class Config:
#         orm_mode = True
