import os
from fastapi import FastAPI, Header, HTTPException, status,Depends,Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi.security import APIKeyHeader
import psycopg2
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
app = FastAPI()
 
#db connection
def get_connection():
    return psycopg2.connect(
        dbname="test",       # your database name
        user="postgres",       # your db user
        password="danish@552", # your db password
        host="localhost",
        port="5432"
    )

# db connection end


class Employee(BaseModel):
    name: str
    age: int

load_dotenv()
VALID_API_KEY = os.getenv("MY_API_KEY")

app = FastAPI()




# Extract API key from header
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)



@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": str(exc.detail),            # Correct use of str()
            "status_code": exc.status_code         # As a separate field
        }
    )

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc.detail)}
    )
# Validate against .env key
def verify_api_key(x_api_key: str = Depends(api_key_header)):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
    return x_api_key

# Projecct End point
@app.get("/employee/{person_id}",summary="Get the person by the Id",)
def getperson(person_id: int,api_key:str = Depends(verify_api_key)):
    print({"api_key":api_key})
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM apidata WHERE id = %s;", (person_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row:
            return {"id": row[0], "name": row[1], "age": row[2]}
        else:
            return {"message": f"No person found with id {person_id}"}

    except Exception as e:
        raise HTTPException(status_code=500, message=str(e))



@app.post("/employee", summary="Add new Employee")
def insert_data(data: Employee, api_key: str = Depends(verify_api_key)):
    name = data.name
    age = data.age

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM apidata WHERE name = %s AND age = %s;", (name, age))
        existing_record = cur.fetchone()

        if existing_record:
            cur.close()
            conn.close()
            return JSONResponse(
                content={"message": "Employee already exists", "Employee":{"name": name, "age": age}},
                status_code=409,
            )

        cur.execute("INSERT INTO apidata (name, age) VALUES (%s, %s) RETURNING id;", (name, age))
        inserted_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse(content={"message":"Employee successfully registered","Employee":{"id":id,"name":name,"age":age}})
    except Exception as e:
        return {"error": str(e)}


@app.delete("/employee/{id}",summary="Delete employee by ID")
def delete_data(id: int,api_key:str = Depends(verify_api_key)):
    try:
        conn = get_connection()
        cur = conn.cursor()
        # Check if the ID exists first
        cur.execute("SELECT * FROM apidata WHERE id = %s;", (id,))
        row = cur.fetchone()

        if not row:
            cur.close()
            conn.close()
            return {"message": f"No record found with ID {id}"}

        # If it exists, delete it
        cur.execute("DELETE FROM apidata WHERE id = %s;", (id,))
        conn.commit()
        cur.close()
        conn.close()
        return {"message": f"Record with ID {id} deleted successfully"}

    except Exception as e:
        return {"message": str(e)}
    
# @app.get("/employee",summary="Show all Employees")
# def get_data():    
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM apidata;")  # your table name
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     # return list of dicts
#     # {"message":"Click on the above button to print all data from data base"}
#     return [{"id": r[0], "name": r[1], "age": r[2]} for r in rows]




