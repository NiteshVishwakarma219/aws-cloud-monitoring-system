import boto3

cloudwatch = boto3.client('cloudwatch')

response = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'YOUR_INSTANCE_ID'
        },
    ],
    StartTime='2025-01-01T00:00:00Z',
    EndTime='2025-01-01T01:00:00Z',
    Period=300,
    Statistics=['Average']
)

print(response)