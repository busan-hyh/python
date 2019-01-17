# INSERT 하기
import datetime
from pymongo import MongoClient as mongo
conn = mongo('mongodb://hyh:1234@192.168.111.101:27017')
db = conn.get_database('test')

# DB 콜렉션 선택
member = db.get_collection('member')

# insert쿼리(insert_one or insert)
# member.insert_one({'uid': 'qwer2', 'pass': 'qwer2', 'name': 'qwer2', 'nick': 'qwe2r2'})

doc = [{'uid': 'qwer3', 'pass': 'qwer3', 'age':45 , 'name': '모니터', 'nick': 'qwe2r3'},
       {'uid': 'qwer4', 'pass': 'qwer4', 'age':23 , 'name': '빅데이터', 'nick': 'qwe2r4', 'rdate': datetime.datetime.now()},
       {'uid': 'qwer5', 'pass': 'qwer5', 'age':56 , 'name': '스크래쳐', 'nick': 'qwe25', 'rdate': datetime.datetime.now()}]
member.insert_many(doc)

print('insert doc')
