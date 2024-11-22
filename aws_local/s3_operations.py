import boto3
from botocore.config import Config

# LocalStack configuration
localstack_endpoint = "http://localhost:4570"

# S3 client configuration
s3_client = boto3.client(
    "s3",
    aws_access_key_id="test",  # Dummy credentials for LocalStack
    aws_secret_access_key="test",
    endpoint_url=localstack_endpoint,
    config=Config(signature_version="s3v4"),
    region_name="us-east-1"
)

# Bucket name and file details
bucket_name = "test-bucket"
file_name = "example.txt"
file_content = "Hello, LocalStack S3, by Lambda!"

def create_bucket_if_not_exists(bucket_name):
    """Create an S3 bucket if it doesn't already exist."""
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' already exists.")
    except:
        print(f"Creating bucket '{bucket_name}'...")
        s3_client.create_bucket(Bucket=bucket_name)

def upload_file_to_s3(bucket_name, file_name, file_content):
    """Upload a file to the specified S3 bucket."""
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=file_content
    )
    print(f"Uploaded '{file_name}' to bucket '{bucket_name}'.")

# Main execution
if __name__ == "__main__":
    create_bucket_if_not_exists(bucket_name)
    upload_file_to_s3(bucket_name, file_name, file_content)
