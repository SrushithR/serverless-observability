"""
    Lambda function to mimic the process of a movie ticket generation
"""
import boto3
import requests

# just add these lines for active tracing of the data flow
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()


def get_object_from_s3():
    """
        Function to connect to s3 and get the data from a file
    :return: None
    """
    s3_client = boto3.client("s3")
    # replace this bucket name with the one you just created
    response = s3_client.get_object(Bucket="meetup-serverless-observability", Key="user_details.json")
    print(response['Body'].read().decode())


def generate_pdf():
    """
        Function to call the generate PDF API
    :return: response of the PDF generation lambda function
    """
    # replace the API url with the one you just created
    url = "https://wf5u5hrui6.execute-api.us-west-2.amazonaws.com/default/pdf_generation"
    response = requests.post(url)
    return response.text


def lambda_handler(event, context):
    """
        Entry function/ main function that will be called first
    :param event: input passed to the lambda function
    :param context: AWS specific variable
    :return: Success message
    """
    print("input to lambda:", event)
    get_object_from_s3()
    generate_pdf()
    return "Success!"
