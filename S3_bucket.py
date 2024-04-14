import boto3


def createS3Bucket(bucket_name):
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket=bucket_name)


createS3Bucket("data2gomobi")