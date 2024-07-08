import boto3
import os

def extract_data():
    s3 = boto3.client('s3')
    bucket_name = 'deeplearning-mlops-demo'
    url = s3.generate_presigned_url(
                    ClientMethod = 'get_object',
                    Params = {'Bucket': bucket_name, 'Key': 'solar_object_detection.zip'},
                    ExpiresIn = 7200
                )
    print(url)
    return url

extract_data()
