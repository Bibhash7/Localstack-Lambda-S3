from aws_local import s3_operations, invoke_lambda_cmd, sqs_queue_operations

if __name__ == '__main__':
    s3_operations.create_bucket_if_not_exists(bucket_name="test-bucket")
    queue_arn = sqs_queue_operations.create_sqs_queue_if_not_exists("super_queue")
    s3_operations.configure_s3_event_notifications(queue_arn=queue_arn, bucket_name='test-bucket')
    s3_operations.upload_file_to_s3(
        bucket_name="test-bucket",
        file_name="example.txt",
        file_content="Hello, LocalStack S3, by Lambda, Created by Bibhash Ghosh!"
    )
    sqs_queue.check_queue_message_count('super_queue')
    invoke_lambda_cmd.invoke_lambda_with_awslocal(
        lambda_name="ReadFileFromS3",
        output_file="./output/output.txt"
    )