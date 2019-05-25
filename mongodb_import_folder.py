import os
import json
from pymongo import MongoClient

path = ''

client = MongoClient('0.0.0.0', 27017)
db = client['testdb']
collection = db['testcol']

for filename in os.listdir(path):
    with open(path+filename) as data:
        json_file = json.load(data)
        collection.insert_one(data)