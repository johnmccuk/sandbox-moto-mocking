import os

# from botocore.exceptions import ClientError
import boto3

# import logging
class TestS3Client:
    def __init__(self):
        self.client = boto3.client("s3", region_name="us-east-1")

    def list_buckets(self):
        return self.client.list_buckets()


def hello_world(event, context):
    client = TestS3Client()
    response = client.list_buckets()

    # Output the bucket names
    print("****" + os.environ["AWS_ACCESS_KEY_ID"])
    print("Existing buckets:")
    for bucket in response["Buckets"]:
        print(f'  {bucket["Name"]}')

    return response["Buckets"]


def lambda_handler(event, context):
    """testing"""
    return hello_world(event, context)


if __name__ == "__main__":
    print("""Please do not execute lambda handler directly.""")
