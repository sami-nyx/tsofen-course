import boto3


def get_vpc_list_regional(region):
    ec2_client = boto3.client('ec2',region)
    response = ec2_client.describe_vpcs()
    return response['Vpcs']


def delete_NATs_in_region(region):
    ec2_client = boto3.client('ec2', region)
    vpcs=get_vpc_list_regional(region)
    gatewaysdesc=ec2_client.describe_nat_gateways()
    # print('========================',region, '========================')
    gateways=gatewaysdesc['NatGateways']
    for gateway in gateways:
        # print(gateway['NatGatewayId'])
        # print(gateway['VpcId'])
        if gateway['State'] != 'deleted':
            nat_gw_id=gateway['NatGatewayId']
            response = ec2_client.delete_nat_gateway(NatGatewayId=nat_gw_id)
            print('detleted nat gateway with id:',nat_gw_id)


def delete_NATs(regions):
    print("deleting NAT gatways...")
    for region in regions:
        delete_NATs_in_region(region["RegionName"])
    print("done.")
