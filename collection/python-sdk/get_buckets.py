import boto3
import uuid

s3client = boto3.client('s3')
list_buckets_resp = s3client.list_buckets()
for bucket in list_buckets_resp['Buckets']:
    print('(Just created) --> {} - there since {}'.format(
        bucket['Name'], bucket['CreationDate']))
