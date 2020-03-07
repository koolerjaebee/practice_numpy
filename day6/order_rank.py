# 정렬과 순위

# 행의 색인이나, 열의 색인 순으로 정렬하는 등의 기준이 필요

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

df = DataFrame(
    np.random.randn(4, 3),
    columns=list('bde'),
    index=['Seoul', 'Busan', 'Daegu', 'Incheon'],
)
format = lambda x: '%.2f' % x

print(df['e'].map(format))

s1 = df['e'].map(format)
print(s1.sort_index())

df2 = DataFrame(
    np.arange(8).reshape(2, 4),
    columns=['d', 'a', 'b', 'c'],
    index=['three', 'one'],
)
print(df2)

print(df2.sort_index())  # row를 기준으로 정렬
print(df2.sort_index(axis=1))  # column 기준으로 정렬

# 데이터(색인과 값)는 기본적으로 오름차순으로 정렬이 된다.
# 내림차순으로 정렬을 할 때는 ascending=False 해준다.
print(df.sort_index(axis=1, ascending=False))

# 객체를 값에 따라 정렬할 경우에는 sort_values 메서드를 사용한다.
obj = Series([4, 7, -3, 1])
print(obj)
print(obj.sort_values())

obj2 = Series([4, np.nan, 8, np.nan, -10, 2])
print(obj2)
print(obj2.sort_values())  # NaN 값은 정렬시 가장 마지막에 위치한다.

frame = DataFrame(
    {
        'b': [4, 7, -5, 2],
        'a': [0, 1, 0, 1],
    }
)
print(frame)
print(frame.sort_values(by='b'))  # by 옵션에 정렬하고자하는 column을 넣어준다.
print(frame.sort_values(by=['a', 'b']))  # 정렬 우선순위 설정 가능

print('-'*30)
# 순위를 정하는 함수는 rank() 이다.
obj3 = Series([7, -2, 7, 4, 2, 0, 4])
print(obj3)

print('---순위---')
print(obj3.rank())  # rank는 동률이 존재할시 rank 범위의 평균값이 나온다. 3, 4위 일시 3.5, 5, 6, 7위 일시 6위

print('---데이터 순서에 따라 순위가 정해짐---')
print(obj3.rank(method='first'))  # 데이터의 순서에 따라 순위를 정하겠다.(동률 x)

print('---내림차순으로 순위를 정하기---')
print(obj3.rank(ascending=False))

print('---내림차순 순서에 따라 순위 정하기---')
print(obj3.rank(ascending=False, method='first'))

print(obj3)
print('---내림차순 그룹지어서 순위를 매김---')
print(obj3.rank(ascending=False, method='max'))  # 중복되면 순위의 큰 값으로 정한다. 3, 4위 일시 4위, 5, 6, 7위 일시 7위
print(obj3.rank(ascending=False, method='min'))  # 중복되면 순위의 작은 값으로 정한다.