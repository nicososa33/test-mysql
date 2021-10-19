# import boto3
# region = 'us-east-1'
# instances = ['i-0b6408134a49efba9']
# ec2 = boto3.client('ec2', region_name=region)
# 
# def lambda_handler(event, context):
#     ec2.stop_instances(InstanceIds=instances)
#     print('stopped your instances: ' + str(instances))

import boto3
# Connect to EC2
ec2 = boto3.client('ec2', region_name='us-east-1')
 

def lambda_handler(event,context):
    custom_filter = [{
        'Name':'tag:Name', 
        'Values': ['MySql_Slave_support']}]
    instances_to_stop = []
    running_instances = ec2.describe_instances(Filters=custom_filter)
    for reservation in running_instances.get('Reservations'):
        for instance in reservation.get('Instances'):
            instances_to_stop.append(instance.get('InstanceId'))
    print(f'Stopping following instance Ids : {instances_to_stop}')
    response = ec2.stop_instances(InstanceIds=instances_to_stop)
    print(response)
