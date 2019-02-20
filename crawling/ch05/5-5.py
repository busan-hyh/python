# 시각화 패키지 MatPlotlib

import matplotlib.pyplot as plt

# # 기본 플로차트
# plt.title('Plot1')
# # y축 값 넣기
# plt.plot([1,3,4,6,10,49])
# plt.show()

# # x축 값도 지정하기
# plt.title('Plot2')
# plt.plot([10,20,30,40],
#          [3,6,1,5])
# plt.show()

# # 그래프 스타일
# plt.title('Plot3')
# plt.plot(['a','b','c','d','e'],[4,7,3,8,3],'bs:')
# plt.grid(True)
# plt.show()

plt.title('Plot4')
plt.plot(['a','b','c','d','e'],
         [4,7,3,8,3],
         c='orange',
         ls='--',
         marker='o')
plt.show()