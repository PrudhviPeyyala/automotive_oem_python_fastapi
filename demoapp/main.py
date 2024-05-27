from fastapi import FastAPI
from pydantic import BaseModel
import database
from automotice_oem import oem_api
# from database import get_database_connection
from models.UserModel import User
from demoapp.user_routes import user_api


app = FastAPI()
app.include_router(oem_api.oem_router)
app.include_router(user_api.user_router)


@app.get("/")
def read_root():
    return {"message": "welcome to FastAPI!"}


@app.get("/user")
async def all_users():
    conn = database.get_database_connection()
    cursor = conn.cursor()
    query = "select * from users"
    cursor.execute(query)
    users = cursor.fetchall()
    return users


@app.post("/user")
async def create_user(user: User):
    conn = database.get_database_connection()
    cursor = conn.cursor()
    query = "insert into users(name,email) values(%s, %s)"
    values = (user.name, user.email)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return user


@app.put("/user/{user_name}")
async def update_user(user_name: str, user: User):
    conn = database.get_database_connection()
    cursor = conn.cursor()
    query = "update users set email=%s where name=%s "
    values = (user.email, user_name)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    return user


@app.delete("/user/{user_name}")
async def delete_user(user_name: str):
    conn = database.get_database_connection()
    cursor = conn.cursor()
    query = "delete from users where name=%s"
    values = (user_name,)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    return "deleted user "+user_name
