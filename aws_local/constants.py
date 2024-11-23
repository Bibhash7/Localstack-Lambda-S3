class SuccessMessage:
    """
    Class contains success scenario messages.
    """
    LAMBDA_EXECUTED_SUCCESSFULLY = "lambda_executed_successfully."
    CREATING_S3_BUCKET = "Creating bucket '{}'..."
    UPLOADING_CONTENT_TO_S3_BUCKET = "Uploaded '{}' to bucket '{}'."


class ErrorMessage:
    """
    Class contains error scenario messages.
    """
    BUCKET_ALREADY_EXISTS = "Bucket '{}' already exists."
    LAMBDA_FAILED = "Command failed with error:"
    EXCEPTION_WHILE_RUNNING_LAMBDA = "An error occurred while executing the command: {}"
    IMPROPER_FORMAT = "Please upload file in .txt format"


class EndPoint:
    """
    Class to store all endpoint urls.
    """
    LOCALSTACK_ENDPOINT = "http://localhost:4570"