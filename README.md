# Localstack-Lambda-S3
It will create and upload content to the s3 bucket and read the content by lambda in localstack environment.

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
