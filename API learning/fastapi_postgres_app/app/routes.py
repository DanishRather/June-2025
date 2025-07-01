# app/routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import crud, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all data
@router.get("/apidata/", response_model=list[schemas.ApiData])
def read_apidata(db: Session = Depends(get_db)):
    return crud.get_all_apidata(db)

# POST new data
@router.post("/apidata/", response_model=schemas.ApiData, status_code=status.HTTP_201_CREATED)
def create_apidata(data: schemas.ApiDataCreate, db: Session = Depends(get_db)):
    return crud.create_apidata(db, data)

# DELETE by id
@router.delete("/apidata/{id}", status_code=status.HTTP_200_OK)
def delete_apidata(id: int, db: Session = Depends(get_db)):
    success = crud.delete_apidata(db, id)
    if success:
        return {"message": f"Record with id={id} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Record not found")





















# # app/routes.py
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from . import crud, schemas, database

# router = APIRouter()

# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # GET all records from apidata
# @router.get("/apidata/", response_model=list[schemas.ApiData])
# def read_apidata(db: Session = Depends(get_db)):
#     return crud.get_apidata(db)

# # POST a new record to apidata
# @router.post("/apidata/", response_model=schemas.ApiData)
# def create_apidata(data: schemas.ApiDataCreate, db: Session = Depends(get_db)):
#     return crud.create_apidata(db, data)




# # app/routes.py
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from . import crud, schemas, database

# router = APIRouter()

# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/items/", response_model=list[schemas.Item])
# def read_items(db: Session = Depends(get_db)):
#     return crud.get_items(db)

# @router.post("/items/", response_model=schemas.Item)
# def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     return crud.create_item(db, item)

# @router.delete("/items/{item_id}", response_model=schemas.Item)
# def delete_item(item_id: int, db: Session = Depends(get_db)):
#     db_item = crud.delete_item(db, item_id)
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return db_item
