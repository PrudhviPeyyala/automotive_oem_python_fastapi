from fastapi import APIRouter

from demoapp import database
from demoapp.models.AutomotiveModel import AutoOem

oem_router = APIRouter(prefix="/oem")


@oem_router.get("/all_oems")
async def get_oem():
    conn = database.get_database_connection()
    cursor = conn.cursor()
    query = "select * from oem_oemdetail"
    cursor.execute(query)
    oems = cursor.fetchall()
    return oems


@oem_router.post("/add_oem")
async def add_oem(oem: AutoOem):
    conn = database.get_database_connection()
    cursor = conn.cursor()
    query = "insert into oem_oemdetail(manufacturer,oemModel,yearModel,origin) values(%s,%s,%s,%s)"
    values = (oem.manufacturer, oem.oemModel, oem.yearModel, oem.origin)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return oem


@oem_router.put("/update_oem")
async def update_oem(oem: AutoOem):
    conn = database.get_database_connection()
    cursor = conn.cursor()
    query = "update oem_oemdetail set yearModel=%s where manufacturer=%s and oemModel=%s"
    values = (oem.yearModel, oem.manufacturer, oem.oemModel)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return oem


@oem_router.delete("/delete_oem/{oem_model}")
async def delete_oem(oem_model: str):
    conn = database.get_database_connection()
    cursor = conn.cursor()
    query = "delete from oem_oemdetail where oemModel=%s"
    values = (oem_model,)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return "deleted oem model " + oem_model
