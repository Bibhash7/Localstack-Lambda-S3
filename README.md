# Localstack-Lambda-S3
This project demonstrates the integration of AWS services (S3 and Lambda) using LocalStack. It includes Python modules to:

- Create an S3 bucket.
- Upload a file to the S3 bucket with proper exception handling.
- Deploy a Lambda function in LocalStack that reads the content of a file stored in S3.
- The code is modular, scalable, and designed for easy extension.

## Features
- **S3 Bucket Operations:**
        Creation of S3 buckets.
- File upload with detailed error handling.
- **Lambda Deployment:**
        A Lambda function deployed to LocalStack that reads the content of a file from the S3 bucket.
- **LocalStack Integration:**
        Simulates AWS services locally for testing and development without incurring cloud costs.

## Project Structure
```plaintext
├── LocalStack-Lambda/
|   ├── aws_local/
|   |   ├── client_config.py                 # creates a aws local stack service
|   |   ├── constants.py                     # Store common reusable components 
|   |   ├── invoke_lambda_cmd.py             # Invoke the lambda 
|   |   ├── lambda_read.py                   # Lambda file that is deployed to LocalStack
|   |   ├── s3_operations.py                 # To create and upload content to s3 bucket
|   ├── output/
|   |   ├── output.txt                       # The output of the application
├── main.py                                  # Entry point of the application
├── docker-compose.yml                       # Docker Compose file for setting up development and production environments
└── README.md                                # Project documentation
```
