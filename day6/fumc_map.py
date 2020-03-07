# 함수 적용과 매핑

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# numpy.random 모듈에 있는 randn 함수는 임의 정규분표 데이터를 생성한다.
df = DataFrame(
    np.random.randn(4, 3),
    columns=list('bde'),
    index=['Seoul', 'Busan', 'Daegu', 'Incheon'],
)
print(df)

# 절댓값
print(np.abs(df))

# apply 함수 적용 (행에 대한)
f = lambda x:x.max()-x.min()
print(df.apply(f))

# 열에 대한 함수 적용
print(df.apply(f, axis=1))


def f2(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
print(df.apply(f2))

# DataFrame 객체에서 실수 값을 문자열 포맷으로 변환 할 경우 applymap함수를 사용한다.
format = lambda x: '%.2f' % x
print(df.applymap(format))

# Series 객체에서 실수 값을 문자열 포맷으로 변환할 경우 map 함수를 사용한다.
print(df['e'].map(format))