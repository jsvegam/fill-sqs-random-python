import json
import random
import boto3
from datetime import date
import calendar
pipeline = boto3.client('codepipeline')




# Create SQS client
sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/806175290270/rojo'

equipoNegro = ['Hugo','Martín','Eduardo','Sebastián']
print(equipoNegro)
equipoRojo = ['Carlos','Diego','Rubén','Elvis']

equipoNegro = random.sample(equipoNegro, len(equipoNegro))
print(equipoNegro)
def lambda_handler(event, context):
    # TODO implement
    
    for i in equipoNegro:

        # elemenToDelete = random.choice(equipoNegro)
        # print(elemenToDelete)
        
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
                    'StringValue': 'Negro'
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
