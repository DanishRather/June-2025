from peewee import Model, CharField, IntegerField
from .database import db

class BaseModel(Model):
    class Meta:
        database = db

class Student(BaseModel):
    name = CharField()
    age = IntegerField()
