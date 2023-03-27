import pytest
import boto3
from moto import mock_s3
import os


@pytest.fixture(scope="module")
def aws_credentials():
    """Mocked AWS credentials for moto.  This is really important as a protective measure to avoid
    accidentally interacting with real AWS services based on your default credentials or current
    environment variables."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture
def create_mock_s3(aws_credentials):
    with mock_s3():
        client = boto3.client("s3", region_name="us-east-1")
        yield client
