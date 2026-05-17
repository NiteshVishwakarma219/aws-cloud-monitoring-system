import boto3
import time
from datetime import datetime, timedelta

logs_client = boto3.client('logs')

LOG_GROUP = "/aws/ec2/system-logs"

def fetch_logs(log_stream_name):
    try:
        response = logs_client.get_log_events(
            logGroupName=LOG_GROUP,
            logStreamName=log_stream_name,
            startFromHead=True
        )

        print(f"\n📜 Logs from stream: {log_stream_name}\n")

        for event in response['events']:
            timestamp = datetime.fromtimestamp(event['timestamp'] / 1000)
            message = event['message']
            print(f"[{timestamp}] {message}")

    except Exception as e:
        print(f"[ERROR] Unable to fetch logs: {str(e)}")


def get_latest_stream():
    streams = logs_client.describe_log_streams(
        logGroupName=LOG_GROUP,
        orderBy='LastEventTime',
        descending=True
    )

    if streams['logStreams']:
        return streams['logStreams'][0]['logStreamName']
    return None


if __name__ == "__main__":
    while True:
        stream = get_latest_stream()

        if stream:
            fetch_logs(stream)
        else:
            print("[INFO] No log streams found")

        time.sleep(60)