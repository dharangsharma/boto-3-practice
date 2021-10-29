import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
""" table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
 """

table = dynamodb.Table('users')

""" # Print out some data about the table.
print(table.creation_date_time) """

""" table.put_item(
    Item = {
        'username' : 'Dharangsharma',
        'firstname' : 'Dharang',
        'last_name' : 'Sharma',
        'age' : '25',
        'account_type' : 'standard_user'
    }
)
 """

response = table.get_item(
     Key = {
         'username' : 'Dharangsharma',
         'last_name' : 'Sharma'
     }
)

item = response['Item']
print(item)
