import boto3 
client = boto3.client('dynamodb') 
table = client.create_table( 
    TableName='netflix_cleaned', 
    KeySchema=[ 
        {'AttributeName': 'show_id', 'KeyType': 'HASH'},   # Partition key  
        ], 
        AttributeDefinitions=[ 
            {'AttributeName': 'show_id', 'AttributeType': 'S'}, #string 
            ], 
            BillingMode='PAY_PER_REQUEST', 
            ) 
print("Table successfully created")
