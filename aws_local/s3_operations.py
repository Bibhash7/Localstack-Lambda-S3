from aws_local.constants import EndPoint, SuccessMessage, ErrorMessage
from aws_local.client_config import create_aws_local_service


s3_client = create_aws_local_service("s3", EndPoint.LOCALSTACK_ENDPOINT)
def create_bucket_if_not_exists(bucket_name):
    """
    Create an S3 bucket if it doesn't already exist.
    :param bucket_name
    :return None
    """
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print(ErrorMessage.BUCKET_ALREADY_EXISTS.format(bucket_name))
    except:
        print(SuccessMessage.CREATING_S3_BUCKET.format(bucket_name))
        s3_client.create_bucket(Bucket=bucket_name)

def upload_file_to_s3(bucket_name, file_name, file_content):
    """
    Upload a file to the specified S3 bucket.
    :param bucket_name
    :param file_name
    :param file_content
    :return None
    """
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=file_content
    )
    print(SuccessMessage.UPLOADING_CONTENT_TO_S3_BUCKET.format(file_name, bucket_name))

def configure_s3_event_notifications(queue_arn, bucket_name):
    s3_client.put_bucket_notification_configuration(
        Bucket=bucket_name,
        NotificationConfiguration={
            'QueueConfigurations': [
                {
                    'QueueArn': queue_arn,
                    'Events': ['s3:ObjectCreated:*']
                }
            ]
        }
    )
    print("S3 event notifications configured.")
