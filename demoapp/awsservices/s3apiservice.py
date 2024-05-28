import json

import boto3
from boto3.session import Session
import pandas as pd
import requests


def s3client():
    s3 = boto3.client(
        service_name='s3',
        aws_access_key_id='prud1994',
        aws_secret_access_key='prud1994',
        endpoint_url='http://localhost:4566'
    )
    return s3


def get_s3_buckets():
    response = s3client().list_buckets()
    return pd.json_normalize(response['Buckets'])


def create_s3_bucket(bucket_name: str):
    s3client().create_bucket(Bucket=bucket_name)


def storeObjectToFile(bucket_name: str):
    url = "https://ok.surf/api/v1/cors/news-section-names"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        s3client().put_object(Bucket=bucket_name, Key='news_data_config.json', Body=json.dumps(data))


def get_contents_in_bucket(bucket_name: str):
    response = s3client().list_objects(Bucket=bucket_name)
    contents = pd.json_normalize(response['Contents'])
    return contents
