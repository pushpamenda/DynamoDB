import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Create a table with LSI
table_name = "Orders"

response = dynamodb.create_table(
    TableName=table_name,
    AttributeDefinitions=[
        {'AttributeName': 'UserID', 'AttributeType': 'S'},
        {'AttributeName': 'OrderDate', 'AttributeType': 'S'},
        {'AttributeName': 'OrderAmount', 'AttributeType': 'N'}
    ],
    KeySchema=[
        {'AttributeName': 'UserID', 'KeyType': 'HASH'},       # Partition Key
        {'AttributeName': 'OrderDate', 'KeyType': 'RANGE'}    # Sort Key
    ],
    LocalSecondaryIndexes=[
        {
            'IndexName': 'OrderAmountIndex',
            'KeySchema': [
                {'AttributeName': 'UserID', 'KeyType': 'HASH'},      # Same partition key
                {'AttributeName': 'OrderAmount', 'KeyType': 'RANGE'} # Different sort key
            ],
            'Projection': {
                'ProjectionType': 'ALL'   # ALL | KEYS_ONLY | INCLUDE
            }
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

print("Table with LSI created:", response)
