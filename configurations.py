from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://indupriya1905:GGMgW2Z7koaTbqVG@indupriyan19.7kkm43v.mongodb.net/?retryWrites=true&w=majority&appName=IndupriyaN19"

client = MongoClient(uri, server_api=ServerApi("1"))

db=client.todo_db
collection = db["todo_data"]
