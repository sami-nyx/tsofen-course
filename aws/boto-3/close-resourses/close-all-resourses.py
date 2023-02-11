import os
import boto3
import json
import gateways
import instances
from botocore.config import Config

def get_all_regions():
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_regions()
    return response['Regions']
    

regions = get_all_regions()
instances.terminate_all_ec2_instances(regions)
gateways.delete_NATs(regions)
