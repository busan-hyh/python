# 몽고DB접속하기

from pymongo import MongoClient as mongo

# 몽고DB커넥트 정보 표기방법
conn = mongo('mongodb://hyh:1234@192.168.111.101:27017')

# DB 선택
db = conn.get_database('test')

# 컬렉션 조회(쿼리)
collects = db.list_collection_names()
print(collects)