import boto3
import time
from pythonjsonlogger import jsonlogger
import os

logger = JSONLogger()

def get_instances():
    ec2 = boto3.client('ec2')

    # Use the client to get information about instances
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-code',
                'Values': ['16']
            },
            {
                'Name': 'tag:k8s.io/role/master',
                'Values': ['1']
            }
        ]
    )

    # Extract the instance information from the response
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)

    # Create a list to store instance details
    instances_info = []

    # Extract the instance IDs and instance names
    for instance in instances:
        instance_id = instance['InstanceId']
        instance_name = next((tag['Value']
                              for tag in instance['Tags'] if tag['Key'] == 'Name'), 'Unnamed')
        instances_info.append({"Instance ID": instance_id, "Instance Name": instance_name})

    return instances_info

def main():
    # קריאה למשתנה סביבתי שמגדיר את הזמן בין רצות הקוד (בשניות)
    interval_seconds = int(os.getenv("RUN_INTERVAL_SECONDS", 300))

    while True:
        # Get instances information
        instances_info = get_instances()

        # Log the instances information using json-logger
        logger.info("Instance information", extra={"instances": instances_info})

        # Wait for the specified interval
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()
