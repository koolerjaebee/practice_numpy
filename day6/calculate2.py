# DataFrame과 Series간의 연산 (numpy의 브로드캐스팅과 유사하다.)

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

arr = np.arange(12.).reshape(3, 4)
print(arr)
print(arr[0])

print(arr - arr[0])  # 각 인덱스를 전부 계산

df = DataFrame(
    np.arange(12).reshape(4, 3),
    columns=list('bde'),
    index=['Seoul', 'Kwangju', 'Daegu', 'Incheon']
)
print(df)

s1 = df.ix[0]
print(s1)

print(df-s1)  # 브로드캐스팅

s2 = Series(range(3), index=list('bef'))
print(s2)

print(df+s2)  # 존재하는 색인만 계산

s3 = df['d']
print(s3)

print(df+s3)  # 원하는 방식이 아님

# 행에 대한 연산을 수행할 경우에는 연산 함수를 이용한다.
print(df)
print(df.add(s3, axis=0))
print(df.sub(s3, axis=0))