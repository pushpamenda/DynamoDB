import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Table name
table_name = "OrdersWithGSI"

response = dynamodb.create_table(
    TableName=table_name,
    AttributeDefinitions=[
        {'AttributeName': 'UserID', 'AttributeType': 'S'},      # Base table PK
        {'AttributeName': 'OrderDate', 'AttributeType': 'S'},   # Base table SK
        {'AttributeName': 'ProductID', 'AttributeType': 'S'},   # GSI PK
    ],
    KeySchema=[
        {'AttributeName': 'UserID', 'KeyType': 'HASH'},         # Partition Key
        {'AttributeName': 'OrderDate', 'KeyType': 'RANGE'}      # Sort Key
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'ProductIndex',
            'KeySchema': [
                {'AttributeName': 'ProductID', 'KeyType': 'HASH'}   # GSI Partition Key
            ],
            'Projection': {
                'ProjectionType': 'ALL'   # ALL | KEYS_ONLY | INCLUDE
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print(" Table with GSI created:", response['TableDescription']['TableName'])
