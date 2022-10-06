import pymongo
from decouple import config

DB_PASSWORD = config("db_password")
client = pymongo.MongoClient(f"mongodb+srv://quyenld9699:{DB_PASSWORD}@expressjs-db.uyl3y8e.mongodb.net/?retryWrites=true&w=majority")
db = client.test
