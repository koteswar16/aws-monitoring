import boto3
from aws_monitoring.extensions import base

class EC2KeyPairs(base.ExtensionAPI):

    """APIs for EC2 key pairs."""

    def initialize(self):
        self.ec2 = boto3.client('ec2')

    def claim(self):
        return self.ec2.delete_key_pair(KeyName="my-key-pair")

    def run(self):
        return self.ec2.describe_key_pairs()

    def dry_run(self):
        pass

