from pymongo import MongoClient


try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['optimizer_portfolio']
except Exception as ex:
    print(f'Error connection to db: {ex}')
