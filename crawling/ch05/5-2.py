# 데이터프레임 : 컬럼명이 있는 자료형
import pandas as pd

df1 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
# print(df1)

# 컬럼명 지정한 데이터프레임
df2 = pd.DataFrame({
                        'name' : ['김유신','김춘추','강감찬','이순신'],
                        'age' : [19,21,32,43],
                        'height' : [171,178,181,175]
                    })
# print(df2)

# 데이터 출력
print(df2['name'])
print(df2['age'])
print(df2['height'])