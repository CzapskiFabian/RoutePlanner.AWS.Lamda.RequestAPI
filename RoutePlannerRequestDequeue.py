import boto3
import json


def lambda_handler(event, context):
    # Create SQS client
    sqs = boto3.client('sqs')

    queue_url = 'https://sqs.us-east-2.amazonaws.com/218883686889/RoutePlannerRequests.fifo'

    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=10,
        WaitTimeSeconds=0
    )

    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )

        return message
    else:
        raise Exception('No Content: The queue is empty')