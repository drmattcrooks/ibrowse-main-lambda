import json
import numpy as np

print("loading lambda")


def lambda_handler(event, context):
    question = "A question"
    return {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": { "headerName": "headerValue"},
        "body": f"{json.dumps({'Matt Says': f'A Random Number: {1}'})}"
    }
