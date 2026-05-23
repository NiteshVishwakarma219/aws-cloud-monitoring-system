import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instance_status()

for status in response['InstanceStatuses']:
    print("Instance ID:", status['InstanceId'])
    print("State:", status['InstanceState']['Name'])