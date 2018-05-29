import boto3

ec2 = boto3.client('ec2')
#response = ec2.describe_instances(Filters={'instance-state-name': 'running'})
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
print(response)
