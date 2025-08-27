import boto3
import csv
client = boto3.client('dynamodb')
with open('netflix.csv','r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        client.put_item(
            TableName='netflix',
            Item={
                'show_id':{'S':row['show_id']},
                'type':{'S':row['type']},
                'title':{'S':row['title']},
                'director':{'S':row['director']},
                'cast':{'S':row['cast']},
                'country':{'S':row['country']},
                'date_added':{'S':row['date_added']},
                'release_year':{'N':row['release_year']} if row['release_year'].isdigit() else {'S':row['release_year']},
                'rating':{'S':row['rating']},
                'duration':{'S':row['duration']},
                'listed_in':{'S':row['listed_in']},
                'description':{'S':row['description']}

            }
        )
print('CSV data inserted into DynamoDB Successfully...')