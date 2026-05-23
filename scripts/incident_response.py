import boto3

ec2 = boto3.client('ec2')

instance_id = 'YOUR_INSTANCE_ID'

response = ec2.reboot_instances(
    InstanceIds=[instance_id]
)

print("Reboot initiated")