import json
import decimal
from . constants import *
from botocore.exceptions import ClientError


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def read(table_name, year, title):
    table = dynamodb.Table(table_name)
    try:
        response = table.get_item(
            Key={
                'year': year,
                'title': title
            }
        )
    except ClientError as e:
        return e.response['Error']['Message']
    else:
        item = response['Item']
        return item

def read_table(table_name):
    table = dynamodb.Table(table_name)
    try:
        response = table.scan()
    except ClientError as e:
        return e.response['Error']['Message']
    else:
        item = response
        return item

def create(table_name, title, year, info):
    table = dynamodb.Table(table_name)
    response = table.put_item(
        Item={
            'year': year,
            'title': title,
            'info': info
        }
    )
    return response

def update(table_name, year, title, rating, plot):
    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating = :r, info.plot=:p",
        ExpressionAttributeValues={
            ':r': rating,
            ':p': plot
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

def delete(table_name, title, year):
    table = dynamodb.Table(table_name)
    try:
        response = table.delete_item(
            Key={
                'year': year,
                'title': title
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            return e.response['Error']['Message']
        else:
            raise
    else:
        return response
