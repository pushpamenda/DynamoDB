import boto3
import csv

client = boto3.client('dynamodb')

with open('netflix.csv', 'r', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        client.put_item(
            TableName='netflix',
            Item={
                'show_id': {'S': row['show_id']},   # must match your table key
                'type': {'S': row['type']} if row['type'] else {'S': 'Unknown'},
                'title': {'S': row['title']} if row['title'] else {'S': 'Unknown'},
                'director': {'S': row['director']} if row['director'] else {'S': 'Unknown'},
                'cast': {'S': row['cast']} if row['cast'] else {'S': 'Unknown'},
                'country': {'S': row['country']} if row['country'] else {'S': 'Unknown'},
                'date_added': {'S': row['date_added']} if row['date_added'] else {'S': 'Unknown'},
                'release_year': {'N': row['release_year']} if row['release_year'].isdigit() else {'S': row['release_year']},
                'rating': {'S': row['rating']} if row['rating'] else {'S': 'Unknown'},
                'duration': {'S': row['duration']} if row['duration'] else {'S': 'Unknown'},
                'listed_in': {'S': row['listed_in']} if row['listed_in'] else {'S': 'Unknown'},
                'description': {'S': row['description']} if row['description'] else {'S': 'Unknown'}
            }
        )

print("CSV data inserted into DynamoDB successfully!")
