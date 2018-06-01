import boto3
from aws_monitoring.extensions import base

class EC2VPCs(base.ExtensionAPI):

    """APIs for EC2 vpcs."""

    def initialize(self):
        self.ec2 = boto3.client('ec2')

    def claim(self):
        pass

    def run(self):
        return self.ec2.describe_vpcs()

    def dry_run(self):
        pass

