import boto3
from aws_monitoring.extensions import base

class EC2Addresses(base.ExtensionAPI):

    """APIs for EC2 IPv4 addresses."""

    def initialize(self):
        self.ec2 = boto3.client('ec2')

    def claim(self):
        pass

    def run(self):
        pass

    def dry_run(self):
        pass

