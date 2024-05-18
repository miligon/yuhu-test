from celery import shared_task
import boto3
from django.conf import settings

@shared_task()
def send_task_email(task_id, title, content, email, subscribe=False):
    # Initialize the SNS client
    sns_client = boto3.client('sns', region_name='eu-central-1', 
                              aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
                              aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    subject = f'New Task Created: {title}'
    message = f'Task ID: {task_id}\nTitle: {title}\nContent: {content}'

    if subscribe:
        response = sns_client.subscribe(
            TopicArn='arn:aws:sns:eu-central-1:999305314158:YuhuTest',
            Protocol='email',
            Endpoint=email
        )  

    response = sns_client.publish(
        TopicArn='arn:aws:sns:eu-central-1:999305314158:YuhuTest',
        Message=message,
        Subject=subject,
        MessageStructure='string'
        
    )

    return response