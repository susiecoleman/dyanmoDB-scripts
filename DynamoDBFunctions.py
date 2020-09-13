import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('TABLE_NAME')
table2 = dynamodb.Table('TABLE_NAME')

def get_item(id):
    item = table.query(KeyConditionExpression=Key('id').eq(id))
    return item['Items'][0]

def scan_table():
    response = table.scan()
    items = response['Items']

def scan_filter(value):
    response  = table.scan(FilterExpression=Attr('value').eq(value))['Items']

def scan_filter_large_table(value):
    response = table.scan(Select= 'ALL_ATTRIBUTES',
              FilterExpression=Attr('value').eq(value))
    items = response['Items']

    while response.get('LastEvaluatedKey'):
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'], Select= 'ALL_ATTRIBUTES',
              FilterExpression=Attr('value').eq(value))
        items.extend(response['Items'])

def update_item(id, new_val1, new_val2):
    table.update_item(
    Key={'d': id},
    UpdateExpression='SET value = :x, value2 = :y',
    ExpressionAttributeValues={':x': new_val1, ':y': new_val2}
    )
