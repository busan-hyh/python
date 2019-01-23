from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop

# 네임서버 접속세팅
hdfs = hadoop(user_name='hadoop', port=50070, host='192.168.111.101')

# 디렉터리 조회
#dir = hdfs.list_dir('/')
#print(dir)

# 디렉터리 생성
#hdfs.make_dir('/test2')

# 파일백업(text.txt를 하둡으로)
title = 'hello~HADOOP~'
hdfs.create_file('/test2/test.txt', title, overwrite=True)
print('파일저장완료')