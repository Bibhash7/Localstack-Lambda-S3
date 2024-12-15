from aws_local.client_config import create_aws_local_service
from aws_local.constants import EndPoint

sqs = create_aws_local_service('sqs', EndPoint.LOCALSTACK_ENDPOINT)
def create_sqs_queue_if_not_exists(queue_name):
    """
    Creates an SQS queue if not exists:
    :param queue_name: (String)
    :return: queue_arn (String)
    """
    try:
        response = sqs.get_queue_url(QueueName=queue_name)
        queue_url = response['QueueUrl']
        print(f"SQS queue '{queue_name}' already exists with URL: {queue_url}")
        queue_arn = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=["QueueArn"])["Attributes"]["QueueArn"]
        return queue_arn
    except sqs.exceptions.QueueDoesNotExist:
        response = sqs.create_queue(QueueName=queue_name)
        queue_url = response['QueueUrl']
        print(f"SQS queue '{queue_name}' created with URL: {queue_url}")
        queue_arn = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=["QueueArn"])["Attributes"]["QueueArn"]
        return queue_arn

def check_queue_message_count(queue_name):
    """
    Check the number of messages in the SQS queue.
    :param queue_name: (String)
    :return: message_count (Int)
    """
    queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']
    attributes = sqs.get_queue_attributes(
        QueueUrl=queue_url,
        AttributeNames=['ApproximateNumberOfMessages']
    )
    message_count = int(attributes['Attributes']['ApproximateNumberOfMessages'])
    print(f"The queue '{queue_name}' has {message_count} messages.")
    return message_count