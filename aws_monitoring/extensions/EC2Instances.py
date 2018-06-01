import boto3
from aws_monitoring.extensions import base

class EC2Instances(base.ExtensionAPI):

    """APIs for EC2 instances."""

    def initialize(self):
        self.ec2 = boto3.client('ec2')

    def claim(self):
        pass

    def run(self):
        print("Getting EC2 instances...")
        return self.ec2.describe_instances()

    def dry_run(self):
        pass

