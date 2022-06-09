import json
import numpy as np

print("loading lambda")


def lambda_handler(event, context):
    search_term = event.get('search_term', 'non-passed')
    return {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": { "headerName": "headerValue"},
        "body": f"{json.dumps({'Search Term': search_term})}"
    }
