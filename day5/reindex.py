from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# 색인(index) 객체

#  pandas의 색인 객체는 표 형식의 데이터에서 각 행과 열에 대한 헤더(이름)
#  와 다른 메타데이터(축의 이름)를 저장하는 객체

#  Serires나 DataFrame 객체를 생성할 때 사용되는 배열이나 또는 순차적인 이름은 내부적으로 색인으로 변환된다.

obj = Series(range(3), index=['a', 'b', 'c'])
print(obj)

idx = obj.index
print(idx)
print(idx[1])
print(idx[1:])

# idx[1] = 'd'  # 색인 객체는 변경할 수 없다. == 에러
# print(idx[1])

index2 = pd.Index(np.arrange(3))
print(index2)

# 재색인(reindex): 새로운 색인에 맞도록 객체를 새로 생성하는 기능
obj = Series([2.3, 4.3, -4.1, 3.5], index=['d', 'b', 'a', 'c'])
print(obj)

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)  # 초과하는 색인은 NaN 값 할당

obj3 = obj.reindex(['a', 'b', 'c', 'c', 'e', 'f'], fill_value=0.0)
print(obj3)  # NaN 대신 0.0으로 할당

df = DataFrame(np.arange(9).reshape(3,3), index=['a', 'b', 'd'], columns=['x', 'y', 'z'])
print(df)

df2 = df.reindex(['a', 'b', 'c', 'd'])
print(df2)  # 없는 색인만 NaN 할당

col = ['x', 'y', 'w', 'z']
df2 = df.reindex(columns=col)  # column도 가능
print(df2)

obj4 = Series(['blue', 'red', 'yellow'], index=[0, 2, 4])
print(obj4)

obj5 = obj4.reindex(range(6), method='ffill')  # 1, 3, 5 색인을 앞 색인 값을 할당 == 보간법
print(obj5)

df3 = df.reindex(index=['a', 'b', 'c', 'd'], method='ffill', columns=col)
print(df3)  # DataFrame에서 보간은 행(row)에 대해서만 이루어진다.(axis=0)

#  재색인은 ix를 이용해서 처리할 수도 있다.
df4 = df.ix[['a', 'b', 'c', 'd'], col]  # 보간은 안됨
print(df4)