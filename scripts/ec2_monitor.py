import boto3
import time

ec2 = boto3.client('ec2')

def get_instance_status(instance_id):
    try:
        response = ec2.describe_instance_status(
            InstanceIds=[instance_id],
            IncludeAllInstances=True
        )

        status_list = response.get('InstanceStatuses', [])

        if not status_list:
            print(f"[WARNING] No status found for {instance_id}")
            return

        for status in status_list:
            instance_state = status['InstanceState']['Name']
            system_status = status['SystemStatus']['Status']
            instance_status = status['InstanceStatus']['Status']

            print(f"\n🔍 Instance ID: {instance_id}")
            print(f"🟢 State: {instance_state}")
            print(f"💻 System Status: {system_status}")
            print(f"⚙️ Instance Status: {instance_status}")

    except Exception as e:
        print(f"[ERROR] Failed to fetch instance status: {str(e)}")


if __name__ == "__main__":
    INSTANCE_ID = "i-xxxxxxxxxxxx"
    
    while True:
        get_instance_status(INSTANCE_ID)
        time.sleep(30)