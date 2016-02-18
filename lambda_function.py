
import json
import boto3

def lambda_handler(event, context):

    ecs_service = 'natetest'
    ecs_cluster = 'default'
    maxCount = 4

    client = boto3.client('ecs')
    services = client.describe_services(cluster=ecs_cluster, services=[ecs_service])['services']
    current_desired_count = services[0].desiredCount
    new_desired_count = current_desired_count
    alarm_object = json.loads(event['Records'][0]['Sns']['Message'])

    if (     alarm_object['NewStateValue'] == "ALARM"
         and alarm_object['OldStateValue'] != alarm_object['NewStateValue']
       ):
        new_desired_count = current_desired_count+1

    if (     alarm_object['NewStateValue'] == "OK"
         and alarm_object['OldStateValue'] != alarm_object['NewStateValue']
       ):
        new_desired_count = current_desired_count-1


    response = client.update_service(
        cluster=ecs_cluster,
        service=ecs_service,
        desiredCount=new_desired_count
    )

    return response


