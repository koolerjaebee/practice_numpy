import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# DataFrame은 2차원 리스트(배열) 같은 자료구조
# R언어 data.frame과 비슷하다.

a = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
print(a)

data = {
    'city': ['서울', '부산', '광주', '대구'],
    'year': [2000, 2001, 2002, 2002],
    'pop': [4000, 2000, 1000, 1000],
}
df = DataFrame(data)
print(df)

df = DataFrame(data, columns=['year', 'city', 'pop'])
print(df)

df2 = DataFrame(data, columns=['year', 'city', 'pop', 'debt'], index=['one', 'two', 'three', 'four'])
print(df2)

print(df2['city'])
print(df2['year'])

print(df2.columns)
print(df2.index)

# print(df2['three']) 에러
print(df2.ix['three'])  # ix: 로우(행)의 위치 접근할 때 사용하는 메소드
# ix는 색인을 name 속성의 값으로 할당한다.

df2['debt'] = 1000  # 모든 값이 1000으로 할당
print(df2)
df2['debt'] = np.arange(4)  # 배열로 할당 가능
print(df2)

val = Series([1000, 2000, 3000, 4000])
df2['debt'] = val
print(df2)  # 바뀌지 않는다 왜냐하면 인덱스가 다르기 때문

val = Series([1000, 2000, 3000, 4000], index=['one', 'two', 'three', 'four'])
df2['debt'] = val
print(df2)

val2 = Series([1000, 3000, 5000], index=['one', 'three', 'four'])
df2['debt'] = val2
print(df2)  # Series를 이용해 원하는 위치에만 데이터를 할당할 수 있다

df2['isSeoul'] = df2.city == '서울'
print(df2)

del df2['isSeoul']
print(df2.columns)
print(df2)

data2 = {
    'seoul': {2001: 20, 2002: 30},
    'busan': {2000: 10, 2001: 200, 2002: 300},
}

df3 = DataFrame(data2)
print(df3)  # 제일 긴 것 기준으로 만들어지고 없는 데이터는 NaN 할당

print(df3.T)  # row랑 col 바꿔서 반환

print(df3.values)  # DataFrame에서 value속성은 2차원 배열로 반환