import boto3
import time

ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

INSTANCE_ID = "i-xxxxxxxxxxxx"

def check_cpu_utilization():
    try:
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': INSTANCE_ID
                }
            ],
            StartTime=time.time() - 300,
            EndTime=time.time(),
            Period=300,
            Statistics=['Average']
        )

        datapoints = response['Datapoints']

        if not datapoints:
            print("[INFO] No CPU data available")
            return 0

        return datapoints[0]['Average']

    except Exception as e:
        print(f"[ERROR] CPU check failed: {str(e)}")
        return 0


def restart_instance():
    try:
        print(f"🔄 Restarting instance {INSTANCE_ID} ...")
        ec2.reboot_instances(InstanceIds=[INSTANCE_ID])
        print("✅ Restart triggered successfully")

    except Exception as e:
        print(f"[ERROR] Restart failed: {str(e)}")


if __name__ == "__main__":
    while True:
        cpu = check_cpu_utilization()
        print(f"🔥 CPU Usage: {cpu}%")

        if cpu > 80:
            print("⚠️ High CPU detected! Triggering auto recovery...")
            restart_instance()

        time.sleep(60)