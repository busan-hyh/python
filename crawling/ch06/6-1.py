# 머신러닝 XOR 연산(sklearn)

from sklearn import svm

# XOR 연산 = 0,0/1,1 이 들어가면 0이, 0,1/1,0 이 들어가면 1이 나오는 연산
xor_data = [[0,0,0],
            [0,1,1],
            [1,0,1],
            [1,1,0]]

# 앞의 0,0 두개는 문제, 뒤의 0은 정답(정답 = label)이므로 문제와 정답을 나눠야 한다.
data = []
label = []

for row in xor_data:
    x = row[0]
    y = row[1]
    z = row[2]

    data.append([x,y])
    label.append(z)

# 데이터 학습 시키기 svm:서포트 벡터 머신 이라는 학습기법 사용
# 즉 svm를 활용해야함
model = svm.SVC()
model.fit(data,label)

# 데이터 예측
pre = model.predict([[1,0],[1,1],[0,1],[0,0]])
print(pre)
