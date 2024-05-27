from fastapi import APIRouter
from demoapp.userservices import userservice

user_router = APIRouter(prefix="/user")


@user_router.get("/alloemusers")
async def getusers():
    users = userservice.users()
    return users
