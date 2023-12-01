import boto3
import os
import time
from pythonjsonlogger import jsonlogger
import logging

# Configure JSON logger
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

def get_instances():
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

    ec2 = boto3.client('ec2', region_name='eu-north-1', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

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

    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)

    return instances

def main():
    while True:
        instances = get_instances()

        instances_info = []
        for instance in instances:
            instance_id = instance['InstanceId']
            instance_name = next((tag['Value']
                                  for tag in instance['Tags'] if tag['Key'] == 'Name'), 'Unnamed')
            instances_info.append({"Instance ID": instance_id, "Instance Name": instance_name})

        # Log the instances information using json-logger
        logger.info("Instance information", extra={"instances": instances_info})

        # Wait for the specified interval (5 minutes)
        time.sleep(300)

if __name__ == "__main__":
    main()
