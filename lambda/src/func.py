import boto3
import json
import os

START_INSTANCES_EVENT = os.environ['START_INSTANCES_EVENT'] if "START_INSTANCES_EVENT" in os.environ else "START_INSTANCES_EVENT"
STOP_INSTANCES_EVENT = os.environ['STOP_INSTANCES_EVENT'] if "STOP_INSTANCES_EVENT" in os.environ is not None else "STOP_INSTANCES_EVENT"
REGION = os.environ["REGION"]
TAG_KEY = os.environ["TAG_KEY"]
TAG_VALUE = os.environ["TAG_VALUE"]
TOPIC_ARN = os.environ["TOPIC_ARN"]


def handler(event, context):
    print(event)
    start_stop_instances(event["eventType"], TAG_KEY, TAG_VALUE)


def start_stop_instances(eventType, tagKey, tagValue):
    rds = boto3.client('rds', region_name=REGION)
    #sns = boto3.client('sns', region_name=REGION)
    instancelist = []
    if(eventType == START_INSTANCES_EVENT):
        instances = rds.describe_instances(
            Filters=[
                {
                    'Name': 'tag:'+tagKey,
                    'Values': [tagValue]
                },
                {
                    'Name': 'instance-state-code',
                    'Values': ["80"],
                }
            ]
        )
        for reservation in (instances["Reservations"]):
            for instance in reservation["Instances"]:
                instancelist.append(instance["InstanceId"])
        if(len(instancelist) > 0):
            print("Started Instances with IDs", instancelist)
            # sns.publish(
            #     TopicArn='arn:aws:sns:us-east-1:974195321489:scheduled-start-stop-topic',
            #     Message="Your Scheduled Event Started {instanceCount} EC2 Instances".format(
            #         instanceCount=len(instancelist)),
            #     Subject="[Scheduled Start Stop] Started instances"
            # )

            rds.start_instances(InstanceIds=instancelist)
        else:
            print("No instances to stop")
    if(eventType == STOP_INSTANCES_EVENT):
        instances = rds.describe_instances(
            Filters=[
                {
                    'Name': 'tag:'+tagKey,
                    'Values': [tagValue]
                },
                {
                    'Name': 'instance-state-code',
                    'Values': ["16"],
                }
            ]
        )
        for reservation in (instances["Reservations"]):
            for instance in reservation["Instances"]:
                instancelist.append(instance["InstanceId"])
        if(len(instancelist) > 0):
            print("Stopped Instances with IDs", instancelist)
            rds.stop_instances(InstanceIds=instancelist)
            # sns.publish(
            #     TopicArn='arn:aws:sns:us-east-1:974195321489:scheduled-start-stop-topic',
            #     Message="Your Scheduled Event Stopped {instanceCount} EC2 Instances".format(
            #         instanceCount=len(instancelist)),
            #     Subject="[Scheduled Start Stop] Stopped instances"
            # )
        else:
            print("No instances to start")
