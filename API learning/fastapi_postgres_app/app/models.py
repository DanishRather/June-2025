
# app/models.py
from sqlalchemy import Column, Integer, String
from .database import Base

class ApiData(Base):
    __tablename__ = "apidata"  # Make sure it matches your existing table

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)



# # app/models.py
# from sqlalchemy import Column, Integer, String
# from .database import Base

# class Item(Base):
#     __tablename__ = "apidata"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     age = Column(Integer, nullable=False)

#     # id = Column(Integer, primary_key=True, index=True)
#     # name = Column(String, index=True)
#     # description = Column(int, index=True)
