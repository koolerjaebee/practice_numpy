# 중복 색인

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj)

# 중복되는 색인 값이 있을 경우에는 색인을 이용한 결과로 Series객체를 반환한다.
print(obj['a'])
print(obj['b'])

# 중복되는 색인값이 얿ㅅ을 경우에는 색인을 이용한 결과로 스칼라 값을 반환한다.
print(obj['c'])

df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df)
print(df.ix['b'])