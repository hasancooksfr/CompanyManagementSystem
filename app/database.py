import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "company_management"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

employees_collection = db['employees']
departments_collection = db['departments']
salary_structure_collection = db['salary_structure']
payrolls_collection = db['payrolls']
attendance_collection = db['attendance']