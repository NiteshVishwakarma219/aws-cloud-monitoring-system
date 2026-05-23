import boto3

logs = boto3.client('logs')

response = logs.describe_log_groups()

for log in response['logGroups']:
    print(log['logGroupName'])