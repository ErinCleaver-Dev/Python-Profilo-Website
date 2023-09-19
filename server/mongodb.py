from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from decouple import config

MONGO_URL = config('MONGO_URL')

def database():
    client = MongoClient(MONGO_URL, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        database = client.neuraldb
        return database
    except Exception as e:
        print(e)
