# 경사하강법 : 데이터 분포도에서 가장 오차가 적은 회귀선을 찾는 것

x_data = [170,155,150,175,165]
y_data = [65,50,45,70,55]

# a는 기울기, b는 절편. a를 구하면 b는 자동으로 구해진다
# eta는 컴퓨터가 반복적으로 대입해볼 차이
a = 0
b = 0
eta = 0.0000075

# true=최적의 기울기를 찾을때(이차함수 기울기가 0이 될때)
while True:
    new_a = a - eta * (x_data[0]*2*(a*x_data[0]+b-y_data[0])+
                       x_data[1]*2*(a*x_data[1]+b-y_data[1])+
                       x_data[2]*2*(a*x_data[2]+b-y_data[2])+
                       x_data[3]*2*(a*x_data[3]+b-y_data[3])+
                       x_data[4]*2*(a*x_data[4]+b-y_data[4]))

    new_b = b - eta * (2*b+2*(x_data[0]*a-y_data[0])+
                       2*b+2*(x_data[1]*a-y_data[1])+
                       2*b+2*(x_data[2]*a-y_data[2])+
                       2*b+2*(x_data[3]*a-y_data[3])+
                       2*b+2*(x_data[4]*a-y_data[4]))

    if a == new_a:
        break

    a = new_a
    b = new_b

    print(a,b)

print('기울기a : ', a)
print('절편b   : ', b)

# 결과
# 기울기a :  0.9767441021911394
# 절편b   :  -102.209288612913