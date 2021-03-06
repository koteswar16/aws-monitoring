import boto3
from aws_monitoring.extensions import base

class EC2Volumes(base.ExtensionAPI):

    """APIs for EC2 volumes."""

    def initialize(self):
        self.ec2 = boto3.client('ec2')

    def claim(self):
        pass

    def run(self):
        print("Getting ec2 volumes...")
        return self.ec2.describe_volumes()

    def dry_run(self):
        pass

