import boto3
from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from typing import Optional

from models import FileValute

app = FastAPI()
# Configure DynamoDB client
dynamodb = boto3.resource('dynamodb',
    endpoint_url='http://localhost:8000',
    region_name='local',
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy'
)
table = dynamodb.Table('YourTableName')


@app.get("/ping"):
def ping():
    return "pong"

@app.post("/api/upload")
async def process_request(user: UserRequest):
    """To proces the client request of updating attachments to s3 bucket and store the details in DynamoDB"""
    # receive the request
    # validate the request
    # generate the unique link
    # craete new request in dynao db
    # upload the file to s3
    # update the link in dynamo db
    return JSONResponse(content={"status": "success", "link": ""}, status_code=201)

@app.get("/api/{unique_id}")
async def get_file_rsponse(user_id: str):
    """To get the user details from DynamoDB"""
    attachment = None
    attachment_name = None
    if attachment:
        return FileResponse(content=attachment, media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={attachment_name}"}, status_code=200)
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)