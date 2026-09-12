import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "company_management"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

employees_collection = db['employees']