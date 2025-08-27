import boto3
import json
client = boto3.client('dynamodb')
with open('netflix_cleaned.json','r') as file:
    data=json.load(file)
    for row in data:
        client.put_item(
            TableName='netflix_cleaned',
            Item={
                'show_id':{'S':row['show_id']},
                'type':{'S':row['type']},
                'title':{'S':row['title']},
                'director':{'S':row['director']},
                'cast':{'S':row['cast']},
                'country':{'S':row['country']},
                'date_added':{'S':row['date_added']},
                'release_year': {'S': str(row['release_year'])},
                'rating':{'S':row['rating']},
                'duration':{'S':row['duration']},
                'listed_in':{'S':row['listed_in']},
                'description':{'S':row['description']}
            }
        )
print('JSON data inserted into DynamoDB Successfully...')