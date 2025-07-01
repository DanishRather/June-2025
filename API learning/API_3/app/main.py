from fastapi import FastAPI,Header
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
import os

app =  FastAPI()
DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/user")
def get_data(Your_name: str = Header(...)):
    return JSONResponse(content={"message":f"Your name is {x_token} ",})