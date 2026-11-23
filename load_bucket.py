import os
from dotenv import load_dotenv
import boto3

# Load environment variables for bucket use
load_dotenv()
bucket_endpoint = os.getenv("AWS_ENDPOINT_URL")
bucket_region = os.getenv("AWS_DEFAULT_REGION")
access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
key_id = os.getenv("AWS_ACCESS_KEY_ID")

bucket_name = "factures"
S3_PATH = "s3://factures"

s3_client = boto3.client("s3")

# Download

def download(storage, local_folder) : 
    paginator = s3_client.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name, Prefix=storage):
        if 'Contents' in page:
            for obj in page['Contents']:
                s3_key = obj['Key']
                print(f"Found in S3: {s3_key}")
            
                # Skip if the key represents the folder itself
                if s3_key == storage:
                    continue
                
                # Compute the local file path
                relative_path = os.path.relpath(s3_key, storage)
                local_path = os.path.join(local_folder, relative_path)
            
                # Ensure the local subdirectories exist
                os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
                s3_client.download_file(bucket_name, s3_key, local_path)
                print(f"Downloaded: s3://{bucket_name}/{s3_key} -> {local_path}")
    print(f"[{storage}] Downloaded into {local_folder}")

# Upload

def upload(local_folder, storage) : 
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)
        
            # Calculate the relative path to keep the directory structure
            relative_path = os.path.relpath(local_path, local_folder)
            s3_path = os.path.join(storage, relative_path).replace("\\", "/")
        
            s3_client.upload_file(local_path, bucket_name, s3_path)
            print(f"Uploaded: {local_path} -> s3://{bucket_name}/{s3_path}")

    print(f"[{local_folder}] Uploaded into {storage}")