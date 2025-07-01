# /app/main.py
from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.db import get_db, ApiData
from app.models import ApiDataCreate, ApiDataResponse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key from the .env file
API_KEY = os.getenv("API_KEY")

# Dependency to verify API key
def verify_api_key(api_key: str = Query(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

# Initialize FastAPI app
app = FastAPI()

# GET endpoint to retrieve data from the database
@app.get("/apidata/{item_id}", response_model=ApiDataResponse)
def get_apidata(item_id: int,db: Session = Depends(get_db)):
    item = db.query(ApiData).filter(ApiData.id == item_id).first()
    item =db.query(ApiData).all()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# POST endpoint to add new data to the database
@app.post("/apidata/", response_model=ApiDataResponse)
def create_apidata(apidata: ApiDataCreate, db: Session = Depends(get_db), api_key: str = Depends(verify_api_key)):
    new_item = ApiData(**apidata.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# DELETE endpoint to delete data from the database
@app.delete("/apidata/{item_id}", response_model=ApiDataResponse)
def delete_apidata(item_id: int, db: Session = Depends(get_db), api_key: str = Depends(verify_api_key)):
    item = db.query(ApiData).filter(ApiData.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return item


