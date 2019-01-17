# INSERT 하기

from pymongo import MongoClient as mongo
conn = mongo('mongodb://hyh:1234@192.168.111.101:27017')
db = conn.get_database('test')

# DB 코렉션 선택
member = db.get_collection('member')

member.insert_one({'uid': 'qwer', 'pass': 'qwer', 'name': 'qwer', 'nick': 'qwer'})
print('insert 1')
