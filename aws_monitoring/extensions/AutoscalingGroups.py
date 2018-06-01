import boto3
from aws_monitoring.extensions import base

class AutoscalingGroups(base.ExtensionAPI):

    """APIs for autoscaling groups."""

    def initialize(self):
        self.autoscale = boto3.client('autoscaling')

    def claim(self):
        pass

    def run(self):
        print("Getting autoscaling groups...")
        return self.autoscale.describe_auto_scaling_groups(
            AutoScalingGroupNames=[
                'my-auto-scaling-group',
            ],
        )

    def dry_run(self):
        pass

