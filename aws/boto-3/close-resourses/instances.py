import boto3


def terminate_instances_in_region(region):
    ec2_resource = boto3.resource('ec2', region)
    all_instances=ec2_resource.instances.all()

    for instance in all_instances:
        if instance.state["Name"] != "terminated":
            print("terminating instance:", instance, "\tin region:", region)
            instance.terminate()


def terminate_all_ec2_instances(regions):
    print("terminating instances...")
    for region in regions:
        terminate_instances_in_region(region["RegionName"])
    print("done.")