# from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="*****",       # your database name
        user="******",       # your db user
        password="******", # your db password
        host="localhost",
        port="5432"
    )

@app.get("/")
def get_data():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM apidata;")  # your table name
    rows = cur.fetchall()
    cur.close()
    conn.close()
    # return list of dicts
    # {"message":"Click on the above button to print all data from data base"}
    return [{"id": r[0], "name": r[1], "age": r[2]} for r in rows]


@app.post("/insert/{name}/{age}")
def insert_data(name: str, age: int):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO apidata (name, age) VALUES (%s, %s) RETURNING id;",
            (name, age)
        )
        inserted_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return {"message": f" Successfully inserted '{name}' (age {age}) with ID {inserted_id}"}
    except Exception as e:
        return {"error": str(e)}


@app.delete("/delete/{id}")
def delete_data(id: int):
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
        return {"error": str(e)}


# @app.post("/apidata/{name}/{age})
# def insert_apidata(name: str, age: int):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO apidata (name, age) VALUES (%s, %s) RETURNING id;",
#         (name, age)
#     )
#     inserted_id = cur.fetchone()[0]
#     conn.commit()
#     cur.close()
#     conn.close()

#     return {"id": inserted_id, "name": name, "age": age}









# @app.get("/")
# def test_db():
#     try:
#         conn = get_connection()
#         conn.close()
#         return {"status": "Connection successful"}
#     except Exception as e:
#         return {"status": "Connection failed", "error": str(e)}


#Root Api testing
# @app.get("/")
# def read_root():
#     return {"Welcome":"Api"}


#geting the items through api
# @app.get("/items/{name}/{roll}/{age}")
# def get_connection():
#     return psycopg2.connect(
#         dbname="testdb",
#         user="postgres",
#         password="your_postgres_password",
#         host="localhost",
#         port="5432"
#     )
# def read_items(name:str,roll:int,age:int):
#     return {"name":name,
#     "roll":roll,
#     "age":age,}
#     # Union[str,none]=none)

# @app.post("/items/{name}/{roll}/{age}")
# def put_items(name:str,roll:int,age:int):
#     return {"name":name,
#     "roll":roll,
#     "age":age,}

# @pp.delete()
