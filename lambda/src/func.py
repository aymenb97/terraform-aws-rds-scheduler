import json
import boto3


def lambda_handler(event, context):
    print(event)
    rds = boto3.client("rds")
    resourceGroup = boto3.client('resourcegroupstaggingapi')
    resources = resourceGroup.get_resources(TagFilters=[{'Key': 'rds-scheduled-start-stop', 'Values':
                                                         ['true']}])

    for res in resources['ResourceTagMappingList']:
        print(rds.describe_db_instances(
            DBInstanceIdentifier=res['ResourceARN']))

    #     print(rds.stop_db_instance(
    #         DBInstanceIdentifier=resource['ResourceARN'].split(":")[6]))

    # db_instances = rds.describe_db_instances()["DBInstances"]
    # print(rds.describe_db_instances(
    #     DBInstanceIdentifier="arn:aws:rds:us-east-1:974195321489:db:database-2"))
    # for instance in db_instances:
    #     print(instance['DBInstanceIdentifier'])
    #     if instance["TagList"][0] == "scheduled" and instance["TagList"][1] == "true":
    #         print(instance)

    # print(rds.describe_db_instances()["DBInstances"])
    # print(rds.stop_db_instance(DBInstanceIdentifier="database-1"))
