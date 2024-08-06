import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    ses_client = boto3.client('ses')
    
    SENDER = "achyuthreddy0110@gmail.com" 
    RECIPIENT = "achyuthreddy0110@gmail.com"
    SUBJECT = "Assignment updates"
    BODY_TEXT = ("This email is sent by AWS SES invoked by a Lambda function \n\n"
                "Task No. 1 and 2 \n\n"
                "As mentioned in the below email, I have created docker files using CMD & ENTRYPOINT \n\n"
                "Using CMD -- docker pull achyuth707/webpage-cmd:latest && docker run -d -p 8080:80 achyuth707/webpage-cmd \n\n"
                "Using ENTRYPOINT -- docker pull achyuth707/webpage-entrypoint:latest && docker run -d -p 8080:80 achyuth707/webpage-entrypoint \n\n"
                "The difference between CMD and ENTRYPOINT is that CMD is flexible and can be overridden, whereas ENTRYPOINT sets a fixed command that cannot be easily overridden, but commands can be appended to ENTRYPOINT. \n\n"
                "Task No. 3 \n\n"
                "I have successfully set up a Kubernetes cluster using Minikube and deployed the 2048 game application on it. The game is accessible via a web browser through a LoadBalancer service. I have documented the steps & configuration in my GitHub repository -- https://github.com/achyuth707/2048-game-on-minikube/ \n\n"
                "Task No. 4 \n\n"
                "Created a VPC and hosted phpMyAdmin Application (backend application in the private subnet) and web service hosted in web server in the public subnet. I have documented the steps & configuration in my GitHub repository -- https://github.com/achyuth707/phpMyAdmin-on-my-AWS-vpc/ \n\n"
                "Task No. 5 \n\n"
                "Hosted phpMyAdmin on minikube cluster. I have documented configuration in my GitHub repository - https://github.com/achyuth707/phpmyadmin-on-minikube/ \n\n"
                "Task No. 6 \n\n"
                "Created a Lambda function to send an email using AWS SES. configuration in my GitHub repository -- https://github.com/achyuth707/Lambda-function-AWS_SES/ \n\n"
                "Task No. 7 \n\n"
                "Created kubernetes deployment on minikube using nginx image. \n\n\n"
                "Best Regards \n"
                "Achyuth Kumar Reddy T\n"
                "+91 9640410258")
    
    try:
        response = ses_client.send_email(
            Source=SENDER,
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ]
            },
            Message={
                'Subject': {
                    'Data': SUBJECT
                },
                'Body': {
                    'Text': {
                        'Data': BODY_TEXT
                    }
                }
            }
        )
    except ClientError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f"Error sending email: {e.response['Error']['Message']}")
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Email sent! Message ID: {response['MessageId']}")
    }
