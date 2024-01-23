from pymongo import MongoClient
from urllib.parse import quote_plus

# Your MongoDB connection string
username = "abdulgafar8281"
password = "Gafar@123"

# Escape the username and password
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# Set up the MongoDB connection
client = MongoClient(f"mongodb+srv://{escaped_username}:{escaped_password}@cluster85.yxziyhj.mongodb.net/?retryWrites=true&w=majority")
db = client['Medical']  # Replace 'medical_inventory' with your preferred database name
users_collection = db['demo2']  # Collection for user data



