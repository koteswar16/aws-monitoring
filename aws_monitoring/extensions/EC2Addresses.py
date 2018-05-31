import boto3
from aws_monitoring.extensions import base

class EC2Addresses(base.ExtensionAPI):

    """APIs for EC2 IPv4 addresses."""

    def initialize(self):
        print("Initializing...")
        self.ec2 = boto3.client('ec2')

    def claim(self):
        return self.ec2.delete_addresses(KeyName="my-address")

    def run(self):
        print("Running...")
        return self.ec2.describe_addresses()

    def dry_run(self):
        pass

