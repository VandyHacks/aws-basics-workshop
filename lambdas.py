# saveNote
import json
import boto3
import time

def lambda_handler(event, context):
    body = json.loads(event["body"])
    dynamo = boto3.client("dynamodb")
    dynamo.put_item(
        TableName="notes",
        Item={
            "name": {
                "S": body["name"]
            },
            "timestamp": {
                "N": str(time.time())
            },
            "data": {
                "S": body["data"]
            }
        }
    )
    return {
        'statusCode': 200,
        'body': "Note saved"
    }


# getNotesByName
import boto3
import json

def lambda_handler(event, context):
    name = event["pathParameters"]["name"]
    dynamo = boto3.client("dynamodb")
    data = dynamo.query(
        TableName="notes",
        KeyConditionExpression='#pk = :pk_val',
        ExpressionAttributeNames={'#pk': "name"},
        ExpressionAttributeValues={':pk_val': {'S': name}}
    )
    return data["Items"]