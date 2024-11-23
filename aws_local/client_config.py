import boto3
from botocore.config import Config

def create_aws_local_service(service_name, endpoint_url):
    """
    This function creates s3 service based on passed service name.
    PS: Although the secrets should be read from a env file, keeping it for future reference.
    :param service_name:
    :param endpoint_url:
    :return: aws_service
    """
    client = boto3.client(
        service_name,
        aws_access_key_id="test",
        aws_secret_access_key="test",
        endpoint_url= endpoint_url,
        config=Config(signature_version="s3v4"),
        region_name="us-east-1"
    )
    return client