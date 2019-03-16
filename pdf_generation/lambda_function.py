import time

def lambda_handler(event, context):
    # mocking the behavior of generating a PDF
    time.sleep(2)
    return "PDF successfully generated"