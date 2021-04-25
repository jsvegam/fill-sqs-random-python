import json
import random
import boto3
from datetime import date
import calendar
pipeline = boto3.client('codepipeline')


# Create SQS client
sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/806175290270/rojo'


def lambda_handler(event, context):
    # TODO implement

    existMembers = is_json_key_present(event, 'miembros')
    existTeam = is_json_key_present(event, 'equipo')
    membersArray = []
    members = ''
    equipo = ''

    if existMembers == True and existTeam == True:
        members = event['miembros']
        equipo = event['equipo']
    
        for m in members:
            membersArray.append(m['nombre'])
    
        membersArray = random.sample(membersArray, len(membersArray))
        print(membersArray)

        for i in membersArray:

            # Send message to SQS queue
            response = sqs.send_message(
                QueueUrl=queue_url,
                DelaySeconds=10,
                MessageAttributes={
                    'Member': {
                        'DataType': 'String',
                        'StringValue': i
                    },
                    'Equipo': {
                        'DataType': 'String',
                        'StringValue': equipo
                    },
                    'WeeksOn': {
                        'DataType': 'String',
                        'StringValue': str(date.today())
                    }
                },
                MessageBody=(
                    'Y el turno es para .....: ' + i + ' , fecha: ' + str(date.today())
                )
            )

    return {
        'statusCode': 200,
        'body': json.dumps('SQS fill').encode('UTF-8')
    }

def is_json_key_present(json, key):
    try:
        buf = json[key]
    except KeyError:
        return False

    return True
        
