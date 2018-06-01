import boto3
from aws_monitoring.extensions import base

class AutoscalingLoadbalancers(base.ExtensionAPI):

    """APIs for autoscaling loadbalancers."""

    def initialize(self):
        self.autoscale = boto3.client('autoscaling')

    def claim(self):
        pass

    def run(self):
        print("Getting autoscaling loadbalancers...")
        return self.autoscale.describe_load_balancers(
            AutoScalingGroupName='my-auto-scaling-group',
        )

    def dry_run(self):
        pass

