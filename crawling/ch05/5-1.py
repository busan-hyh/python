# 파이썬 데이터 분석 실습(numpy)
import numpy as np

# 벡터 생성
list1 = [1,2,3,4,5]# 기본 어레이
vec1 = np.array([1,2,3,4,5])# 넘파이 어레이, 벡터
# print(list1)
# print(vec1)
# print('vec1[0] : ', vec1[0])
# for i in vec1:
#     print(i)

# 넘파이 행렬
mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(mat1)
# print(mat1.T)# 전치행렬, 행과 열이 바뀐다.
# print(mat2)

# 행렬생성 다른방법
mat3 = np.ones([2,4])# 2행 4열이 1로 채워진다.
mat4 = np.zeros([3,2])
# print(mat3)
# print(mat4)

# 단위행렬
mat5 = np.identity(3)# 3행 3열짜리 행렬의 단위행렬
# print(mat5)

# 역행렬
from numpy import linalg

mat7 = np.linalg.inv(mat1)
# print(mat7)

# mat1과 그 역행렬 mat7을 곱하면 단위행렬이 나온다.
mat8 = mat1.dot(mat7)# 자연상수인 1.000e+00 이런게 나오므로 반올림 해야한다.
# print(mat8)

mat9 = mat8.round()
# print(mat9)

# 행렬 슬라이싱, 행렬의 일부만 쓸때 필요
mat10 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(mat10[1,:])# [5 6 7 8]
print(mat10[:,2])# [3 7 11]
print(mat10[:, 0:2])# 전체행, 0에서 2이전까지 열
print(mat10[1:3,:])# 1에서 3이전까지 행, 전체열
print(mat10[0:2, 0:2])
print(mat10[1:3, 1:3])