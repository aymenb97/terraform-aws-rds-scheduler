import json
import boto3
import os


def lambda_handler(event, context):
    start = os.environ['START_EVENT']
    tag_key = os.environ['TAG_KEY']
    tag_value = os.environ['TAG_VALUE']
    stop = os.environ['STOP_EVENT']
    rds = boto3.client("rds")
    if(event['EventType'] == start):
        for db in filter_db_names_by_tag(tag_key, tag_value):
            instance = rds.describe_db_instances(DBInstanceIdentifier=db)
            if instance['DBInstances'][0]['DBInstanceStatus'] != 'available':
                print(rds.start_db_instance(
                    DBInstanceIdentifier=instance['DBInstances'][0]['DBInstanceIdentifier']))
    if(event['EventType'] == stop):
        for db in filter_db_names_by_tag(tag_key, tag_value):
            instance = rds.describe_db_instances(DBInstanceIdentifier=db)
            if instance['DBInstances'][0]['DBInstanceStatus'] != 'stopped':
                print(rds.stop_db_instance(
                    DBInstanceIdentifier=instance['DBInstances'][0]['DBInstanceIdentifier']))


def filter_db_names_by_tag(tag_key, tag_value):
    db_names = []
    resourceGroup = boto3.client('resourcegroupstaggingapi')
    resources = resourceGroup.get_resources(TagFilters=[{'Key': tag_key, 'Values':
                                                         [tag_value]}])
    for res in resources['ResourceTagMappingList']:
        if res["ResourceARN"].split(":")[5] == 'db':
            db_names.append(res["ResourceARN"].split(":")[6])
    return db_names
