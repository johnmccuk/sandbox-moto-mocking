from poetry_demo import handler
import pytest
import os


@pytest.fixture
def s3_add_bucket(create_mock_s3):
    create_mock_s3.create_bucket(Bucket="test01")
    yield


@pytest.fixture
def s3_mocked_bucket(create_mock_s3, s3_add_bucket):
    conn = handler.TestS3Client()
    yield conn


def test_answer(s3_mocked_bucket):
    print("***" + os.getenv("AWS_ACCESS_KEY_ID"))
    print("***" + os.getenv("AWS_SECRET_ACCESS_KEY"))
    print("***" + os.getenv("AWS_SECURITY_TOKEN"))

    result = s3_mocked_bucket.list_buckets()
    assert len(result["Buckets"]) == 1


def test_answer2(s3_mocked_bucket):
    print("***" + os.environ["AWS_ACCESS_KEY_ID"])
    print("***" + os.environ["AWS_SECRET_ACCESS_KEY"])
    print("***" + os.environ["AWS_SECURITY_TOKEN"])

    result = s3_mocked_bucket.list_buckets()
    assert result["Buckets"][0]["Name"] == "test01"
