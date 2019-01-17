#find하기

import datetime
from pymongo import MongoClient as mongo
conn = mongo('mongodb://hyh:1234@192.168.111.101:27017')
db = conn.get_database('test')
member = db.get_collection('member')

#리절트셋으로 파인드 결과를 넣는다. 즉 포문으로 프린트함
"""name만 모두 출력함
rs = member.find()

for doc in rs:
    print(doc['name'])
"""

# 조건문
rs2 = member.find({'uid':'qwer'})

for doc in rs2:
    print(doc['name'])

# and조건문
rs3 = member.find({'uid':'qwer', 'name':'김덕천'})
for doc in rs3:
    print(doc['name'])

