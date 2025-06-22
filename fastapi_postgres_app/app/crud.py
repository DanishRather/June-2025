# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def get_all_apidata(db: Session):
    return db.query(models.ApiData).all()

def create_apidata(db: Session, data: schemas.ApiDataCreate):
    new_entry = models.ApiData(name=data.name, age=data.age)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def delete_apidata(db: Session, id: int):
    entry = db.query(models.ApiData).filter(models.ApiData.id == id).first()
    if entry:
        db.delete(entry)
        db.commit()
        return True
    return False
