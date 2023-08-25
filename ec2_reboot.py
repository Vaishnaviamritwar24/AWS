#import Modules

import boto3
# Set your AWS credentials and region here
aws_access_key = 'AKIA2TWQFX6ZG7NMH7IW'
aws_secret_key = 'c5kCOFotNFdPivAQcS1sZW3wlUmuVuqCPvNxpOBW'
aws_region = 'ap-south-1'

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

#variables
instance_id = [ "i-07f47b2d3677b1bc8" ]

#reboot Logic
#Functions
def reboot(id):
    response = ec2.reboot_instances(InstanceIds=[id,],DryRun=False)
    responsecode = response['ResponseMetadata']['HTTPStatusCode']
    if responsecode == 200:
        print ("Instance ID: {} is rebooted".format(id))
        print ("\n")
    else:
        print ("Instance ID: {} failed to reboot".format(id))
reboot(instance_id[0])
#reboot(instance_id[1])
