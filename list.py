import pandas as pd
from pymongo import MongoClient

# Replace the placeholder with your MongoDB connection string
mongo_uri = 'mongodb+srv://mongo:mongo@mongo.1ics4jt.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(mongo_uri)

# Replace the placeholders with your database and collection names
database_name = 'mltb'
collection_name = 'data'

# Access the specified database and collection
db = client[database_name]
collection = db[collection_name]

# Query MongoDB and convert the result to a DataFrame
cursor = collection.find({}, {'_id': 0})  # Exclude the "_id" field
df = pd.DataFrame(list(cursor))

# Convert the DataFrame to an HTML file
html_table = df.to_html(index=False)

# Save the HTML file
with open('table.html', 'w') as file:
    file.write(html_table)

print("HTML file 'table.html' generated successfully.")
