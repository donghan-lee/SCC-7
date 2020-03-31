from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# db.users.insert_one({'name':'bobby','age':21})

db.users.update_many({'name': 'bobby'}, {'$set': {'age': 22}})
# update_one : 맨 앞 한 명만 / update_many : 전부

all_users = db.users.find()
for user in all_users:
    print(user)