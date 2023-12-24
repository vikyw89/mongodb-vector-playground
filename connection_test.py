from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()
# Replace the placeholder with your Atlas connection string
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# Set the Stable API version when creating a new client
client = MongoClient(MONGO_DB_URL, server_api=ServerApi('1'))
                          
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)