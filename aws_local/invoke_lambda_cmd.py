import subprocess
from aws_local.constants import SuccessMessage, ErrorMessage, EndPoint

def invoke_lambda_with_awslocal(lambda_name, output_file):
    """
    This Functions invokes lambda service deployed in localstack:
    :param lambda_name
    :param output_file
    :return: None
    """
    if not output_file.endswith(".txt"):
        raise Exception(ErrorMessage.IMPROPER_FORMAT)

    command = (
        'awslocal lambda invoke '
        f'--function-name {lambda_name} '
        '--payload "{}" '
        f'{output_file} '
        f'--endpoint-url {EndPoint.LOCALSTACK_ENDPOINT}'
    )

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print(SuccessMessage.LAMBDA_EXECUTED_SUCCESSFULLY)
            print("Output:", result.stdout)
        else:
            print(ErrorMessage.LAMBDA_FAILED)
            print(result.stderr)

    except Exception as error:
        print(ErrorMessage.EXCEPTION_WHILE_RUNNING_LAMBDA.format(error))