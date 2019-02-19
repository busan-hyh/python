# csv파일 임포트
import pandas as pd

df_exam = pd.read_csv('./data/exam.csv')
# print(df_exam)

# 데이터프레임 슬라이스
# print(df_exam[2:4])# 2행에서 4행이전까지 표시. 필요없는 열은 그냥 빼면 되므로 ㄴㄴ

# 파생변수
df_exam['total'] = df_exam.math + df_exam.english + df_exam.science
# print(df_exam[2:4])

df_exam['mean'] = round(df_exam.total / 3)
print(df_exam[2:4])