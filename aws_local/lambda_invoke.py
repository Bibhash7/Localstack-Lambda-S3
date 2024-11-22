from localstack_client import localstack_client

import json

def invoke_lambda():
    client = localstack_client('lambda')

    function_name = "ReadFileFromS3"
    payload = {}

    try:
        response = client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )

        response_payload = json.loads(response['Payload'].read())
        print("Lambda response:", response_payload)
    except Exception as e:
        print(f"Error invoking Lambda: {e}")

# Call the function
invoke_lambda()
