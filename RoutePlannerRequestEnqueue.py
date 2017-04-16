import boto3
import json


def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    return event

    queue_url = 'https://sqs.us-east-2.amazonaws.com/218883686889/RoutePlannerRequests.fifo'

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(event),
        MessageGroupId='MessageGroupId')

    return {"RequestId": response["MessageId"]}