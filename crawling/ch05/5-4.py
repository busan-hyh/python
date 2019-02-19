# 엑셀파일 임포트
import pandas as pd

df_exam = pd.read_excel('./data/exam.xlsx')

# 수학점수 60점이상
df_exam2 = df_exam[df_exam.math >= 60]
# print(df_exam2)

# 정렬
df_exam3 = df_exam2.sort_values(by='math')# 기본 오름차순
# print(df_exam3)
df_exam4 = df_exam2.sort_values(by='math', ascending=False)# 내림차순
# print(df_exam4)

# print(df_exam4.head())
# print(df_exam4.tail())

# 요약통계
print(round(df_exam.describe()))