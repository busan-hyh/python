from pymongo import MongoClient as mongo
conn = mongo('mongodb://hyh:1234@192.168.111.101:27017')
db = conn.get_database('test')
member = db.get_collection('member')

# update하기
member.update_many({'uid':'abcd'},{"$set":{"hp":'63253','pass':'249032'}})
member.update({'uid':'qwer4', 'age':23},{"$set":{"hp":'7869853'}})

# delete하기
member.remove({'age':{'$lt':25}})

print('update!')