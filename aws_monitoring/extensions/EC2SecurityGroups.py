import boto3
from aws_monitoring.extensions import base

class EC2SecurityGroups(base.ExtensionAPI):

    """APIs for EC2 security groups."""

    def initialize(self):
        self.ec2 = boto3.client('ec2')

    def claim(self):
        pass

    def run(self):
        print("Getting ec2 security groups...")
        return self.ec2.describe_security_groups()

    def dry_run(self):
        pass

