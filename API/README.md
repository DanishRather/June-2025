# FastAPI + PostgreSQL API

This FastAPI app allows you to perform GET, POST, and DELETE operations on a PostgreSQL database.

---

##  Requirements

Make sure you have:

- Python 3.8+
- PostgreSQL running (locally or on cloud)

---

##  Setup Instructions

### 1. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate




You can install FastAPI and Uvicorn manually:

pip install fastapi uvicorn psycopg2


 Database Setup
Make sure your PostgreSQL has a database and a table like this:

CREATE TABLE apidata (
    id SERIAL PRIMARY KEY,
    name TEXT,
    value TEXT
);
In your main.py, Change your get_connection according to the db credentials :

def get_connection():
    return psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="localhost",
        port="5432"
    )


🚀 Run the FastAPI App
From the project root:

uvicorn api.main:app --reload
Open your browser:

Docs: http://127.0.0.1:8000/docs

JSON API: http://127.0.0.1:8000/data

📬 API Endpoints
Method	Route	Description
GET	/data	Get all records
POST	/data	Add new record
DELETE	/data/{id}	Delete by ID


