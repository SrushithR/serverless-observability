import boto3
import requests


def get_object_from_s3():
    """
        Function to connect to s3 and get the data from a file
    :return: None
    """
    s3_client = boto3.client("s3")
    response = s3_client.get_object(Bucket="meetup-serverless-observability", Key="user_details.json")
    print(response['Body'].read().decode())


def generate_pdf():
    """
        Function to call the generate PDF API
    :return: response of the PDF generation lambda function
    """
    url = "https://wf5u5hrui6.execute-api.us-west-2.amazonaws.com/default/pdf_generation"
    response = requests.post(url)
    return response.text


# def trigger_email():
#     """
#         Function to trigger an SNS topic
#     :return: None
#     """
#     sns_client = boto3.client("sns")
#     sns_client.publish(
#         TopicArn="arn:aws:sns:us-west-2:392658218916:Ticket-Notification",
#         Message="Ticket Generated",
#         Subject="Ticket!"
#     )


def lambda_handler(event, context):
    print("input to lambda:", event)
    get_object_from_s3()
    generate_pdf()
    trigger_email()


