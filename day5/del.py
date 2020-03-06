import pandas as pd
from pandas import Series, DataFrame
import numpy as np

obj = Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print(obj)

obj2 = obj.drop('c')
print(obj2)

obj3 = obj.drop(['b', 'd'])  # 여러개는 배열 형태로
print(obj3)

df = DataFrame(np.arange(16).reshape(4, 4), index=['Seoul', 'Busan', 'Daegu', 'Incheon'], columns=['one', 'two', 'three', 'four'])
print(df)

new_df = df.drop(['Seoul', 'Busan'])
print(new_df)

new_df = df.drop('three', axis=1)  # col 중 'three'를 지우겠다.
print(new_df)

new_df = df.drop(['two', 'four'], axis=1)
print(new_df)