# 다중 색인(multi index)

# 색인의 계층: pandas의 중요 기능 중의 하나로 다중 색인 단계를 지정할 수 있다.

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

data = Series(
    np.random.randn(11),
    index=[
        ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd'],
        [1, 2, 3, 1, 2, 3, 5, 1, 2, 1, 2]
    ],
)
print(data)
print(data.index)  # index name과 그 라벨(그 리스트의 index)이 나옴

print(data['b'])
print(data['a':'b'])
print(data.ix[['a', 'd']])

print(data[2])  # 이거는 그냥 3번째 데이터
print(data)
print(data[:, 2])
print(data[:, 5])


df = DataFrame(
    np.arnage(12).reshqpe(4, 3),
    index=[
        ['a', 'a', 'b', 'b'],
        [1, 2, 1, 2],
    ],
    columns=[
        ['Seoul', 'Busan', 'Kwangju'],
        ['red', 'green', 'red'],
    ],
)
print(df)
# column index의 이름 정하기
df.columns.name=['city', 'color']
print(df)
df.index.names=['key1', 'key2']
print(df)

print(df['Seoul'])


# 색인 계층의 순서를 바꾸기
# swaplevel() 메서드를 이용해서 바꾼다.
print(df.swaplevel('key1', 'key2'))  # key1과 key2를 바꾸겠다.

# 사전식으로 계층을 바꾸어서 정렬하기
# sortlevel() 메서드를 이용해서 정렬한다.
df2 = df.swaplevel('key1', 'key2')
print(df2.sortlevel(0))  # 어느 깊이의 계층을 할것인지 정해준다.

df3 = df.sortlevel(1)
print(df3.swaplevel(0, 1))  # 숫자를 이용해도 가능

print(df.swaplevel(0, 1).sortlevel(0))

print(df.sortlevel(1).swaplevel(0, 1))
# 전부 다 같은 결과를 낸다.


# sum
print(df)
print(df.sum(level='key2'))  # key2를 기준으로 합

print(df.sum(level='color', axis=1))  # axis 옵션 사용 가능