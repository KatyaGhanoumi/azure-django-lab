import boto3
# Connect to DynamoDB
# boto3 reads your credentials from ~/.aws/credentials (set via aws configure)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Create the table
# DynamoDB uses a primary key--here taskId is the partition key
table = dynamodb.create_table(
TableName='Tasks',
KeySchema=[
{'AttributeName': 'taskId', 'KeyType': 'HASH'}, #partition key
],
AttributeDefinitions=[
{'AttributeName': 'taskId', 'AttributeType': 'S'}, # S String
],
BillingMode='PAY_PER_REQUEST' # free tier: no provisioned capacity needed
)

# Wait for the table to be ready
table.wait_until_exists()
print("Table 'Tasks' created successfully!")
print("Table status:", table.table_status)