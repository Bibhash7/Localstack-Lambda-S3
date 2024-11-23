import boto3
from botocore.config import Config

# LocalStack S3 configuration
localstack_endpoint = "http://host.docker.internal:4570"
s3_client = boto3.client(
    "s3",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    endpoint_url=localstack_endpoint,
    config=Config(signature_version="s3v4"),
    region_name="us-east-1",
)

def lambda_handler(event, context):
    """
    AWS Lambda function to read a file from S3.
    :param event
    :param context
    :return None
    """
    bucket_name = "test-bucket"
    file_name = "example.txt"

    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        file_content = response["Body"].read().decode("utf-8")
        return {
            "statusCode": 200,
            "body": f"File Content: {file_content}",
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error reading file: {str(e)}",
        }
