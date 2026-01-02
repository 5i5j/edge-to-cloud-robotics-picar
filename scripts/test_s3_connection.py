import boto3
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

s3_endpoint = os.getenv('S3_ENDPOINT')
access_key = os.getenv('S3_ACCESS_KEY')
secret_key = os.getenv('S3_SECRET_KEY')
bucket_name = os.getenv('S3_BUCKET_NAME')

def test_connection():
    try:
        s3 = boto3.client(
            's3',
            endpoint_url=f"http://{s3_endpoint}",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        response = s3.list_buckets()
        print("Successfully connected! Buckets:", [b['Name'] for b in response['Buckets']])
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_connection()
