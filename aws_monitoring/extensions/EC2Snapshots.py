import boto3
from aws_monitoring.extensions import base

class EC2Snapshots(base.ExtensionAPI):

    """APIs for EC2 Snapshots."""

    def initialize(self):
        self.ec2 = boto3.client('ec2')

    def claim(self):
        pass

    def run(self):
        print("Getting ec2 snapshots...")
        return self.ec2.describe_snapshots()

    def dry_run(self):
        pass

