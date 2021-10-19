import boto3
 
ec2 = boto3.resource('ec2', region_name='us-east-1')
filters = [
 {'Name': 'owner-id', 'Values': ['103430952571']}, 
 {'Name':'name', 'Values':['MySql_Slave_support']}
]
images = ec2.images.filter(Filters=filters).all()

for image in images:
 print(image.id)
 
AMI = (image.id)
INSTANCE_TYPE = 't3a.micro'
KEY_NAME = 'sqlslave-v'
REGION = 'us-east-1'
SECURITY_GROUP_ID = ['sg-0a0db9858ce867f6c']
 
 
ec2 = boto3.client('ec2', region_name=REGION)
 


def lambda_handler(event, context):
 
 instance = ec2.run_instances(
     ImageId=AMI,
     InstanceType=INSTANCE_TYPE,
     KeyName=KEY_NAME,
     MaxCount=1,
     MinCount=1,
     SecurityGroupIds=SECURITY_GROUP_ID,
     TagSpecifications=[
        {
      'ResourceType': 'instance',
      'Tags': [
        {
          'Key': 'Name',
          'Value': 'MySql_Slave_support'
        },
      ]
    },
  ],
 )
 )
 
 print ("New instance created:")
 instance_id = instance['Instances'][0]['InstanceId']
 print (instance_id)
 
 return instance_id