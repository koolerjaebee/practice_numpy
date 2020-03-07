import pandas as pd
from pandas import Series, DataFrame
import numpy as np

df = DataFrame({
    'a': range(7),
    'b': range(7, 0, -1),
    'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
    'd': [0, 1, 2, 0, 1, 2, 3],
})
print(df)


# set_index 메서드: 하나 이상의 column을 index로 하는 새로운 DataFrame을 생성
print(df.set_index(['c', 'd']))

# 새로운 색인이 되는 데이터를 잃지 않기 위해서라면
# drop 옵션
print(df.set_index(['c', 'd'], drop=False))


# set_index와 반대되는 개념의 메서드: reset_index == index을 column으로
df2 = df.set_index(['c', 'd'])
print(df2)
print(df2.reset_index())  # 앞에 붙음