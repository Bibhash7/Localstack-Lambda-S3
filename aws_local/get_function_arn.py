import boto3
from botocore.config import Config


def get_function_arn():
    localstack_endpoint = "http://localhost:4570"
    lambda_client = boto3.client(
        'lambda',
        aws_access_key_id="test",  # Dummy credentials for LocalStack
        aws_secret_access_key="test",
        endpoint_url=localstack_endpoint,
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",
    )
    print(lambda_client)
    response = lambda_client.list_functions()
    print(response)
    for function in response['Functions']:
        print(f"Function ARN: {function['FunctionArn']}")

get_function_arn()
