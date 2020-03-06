import pandas as pd
from pandas import Series, DataFrame
import numpy as np

obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj['b':'c'])  # b to c

print(obj)

obj['b':'c'] = 10
print(obj)

data = DataFrame(
    np.arange(16).reshape(4, 4),
    index=['Seoul', 'Busan', 'Kwangju', 'Daegu'],
    columns=['one', 'two', 'three', 'four'],
)
print(data)
print(data['two'])
print(data[['one', 'two']])  # list 안에 list를 넣어 슬라이싱

print(data[:2])

print(data[data['three'] > 7])  # 문법 조심

print(data < 5)
data[data < 5] = 0
print(data)

#  ix 속성: DataFrame의 특수한 색인 필드(속성)
print(data.ix['Seoul'])

print(data.ix['Busan', ['two', 'three']])

print(data.ix[['Kwangju', 'Daegu'], ['three', 'four']])

print(data.ix[['Seoul', 'Daegu'], ['three', 'one']])  # 순서도 바꿀 수 있다

print(data.ix[['Daegu', 'Kwangju'], [3, 0, 1]])  # col의 순서에 따른 할당된 숫자로도 호출 가능

print(data.ix[2])
print(data.ix[2, 3])  # 하나의 값을 가져옴

print(data.ix[:'Kwangju', 'three'])  # 여러가지 슬라이싱이 가능하다

print(data.ix[data.three > 5, :3])  # .method도 가능