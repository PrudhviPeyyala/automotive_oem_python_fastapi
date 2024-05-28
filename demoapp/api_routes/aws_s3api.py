from fastapi import APIRouter
from demoapp.awsservices import s3apiservice

aws_router = APIRouter(prefix="/aws")


@aws_router.get("/list_bucket_files")
async def getfilesfrombucket():
    bucket_files = s3apiservice.get_s3_buckets()
    return bucket_files


@aws_router.get("/createbucket/{bucket_name}")
async def createbucket(bucket_name: str):
    s3apiservice.create_s3_bucket(bucket_name)


@aws_router.get("/createfile/{bucket_name}")
async def create_fileinBucket(bucket_name: str):
    s3apiservice.storeObjectToFile(bucket_name)


@aws_router.get("/getobjects/{bucket_name}")
async def get_objs_from_bucket(bucket_name: str):
    return s3apiservice.get_contents_in_bucket(bucket_name)
