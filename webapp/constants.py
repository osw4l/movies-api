import boto3

ACCESS_KEY = 'AKIASUFNBXXYNYS6J4Z4'
SECRET_KEY = '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'

session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

dynamodb = session.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")