from aws_local import s3_operations, invoke_lambda_cmd

if __name__ == '__main__':
    s3_operations.create_bucket_if_not_exists(bucket_name="test-bucket")
    s3_operations.upload_file_to_s3(
        bucket_name="test-bucket",
        file_name="example.txt",
        file_content="Hello, LocalStack S3, by Lambda, Created by Bibhash!"
    )
    invoke_lambda_cmd.invoke_lambda_with_awslocal(
        lambda_name="ReadFileFromS3",
        output_file="./output/output.txt"
    )