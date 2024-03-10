import pandas as pd
from pymongo import MongoClient

# Replace the placeholder with your MongoDB connection string
mongo_uri = 'mongodb+srv://mongo:mongo@mongo.1ics4jt.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(mongo_uri)

# Replace the placeholders with your database and collection names
database_name = 'wzmlx'
collection_name = 'data'

# Access the specified database and collection
db = client[database_name]
collection = db[collection_name]

# Query MongoDB and convert the result to a DataFrame
cursor = collection.find({}, {'_id': 0})  # Exclude the "_id" field
df = pd.DataFrame(list(cursor))

# Display the DataFrame in a structured table format
table = df.to_string(index=False, justify='center')

# Print the formatted table
print(table)
