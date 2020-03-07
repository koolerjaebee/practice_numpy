import pandas as pd
import numpy as np
from numpy import nan as NA
from pandas import Series, DataFrame

# 누락된 데이터 골라내기
# dropna 함수를 이용하는 방법 등 여러 방법이 있을 수 있다.
# dropna를 사용하는 것이 유용한 방법이며, 사용 결과값으로 Series 객체를 반환
data = Series([1, NA, 3.4, NA, 8])
print(data.dropna())

# Boolean index를 이용해서 직접 계산한 후에 가져오기
print(data.notnull())
print(data[data.notnull()])


# DataFrame에서 누락된 데이터를 골라내기
# dropna는 기본적으로 NA값이 하나라도 있는 row는 제외시킨다.
data = DataFrame([
    [1, 5.5, 3],
    [1, NA, NA],
    [NA, NA, NA],
    [NA, 3.3, 3],
])
print(data)
print(data.dropna())

# how='all' 옵션을 주면 모든 값이 NA인 row만 제외된다.
print(data.dropna(how='all'))

data[4] = NA
print(data)
print(data.dropna(how='all', axis=1))

data2 = DataFrame([
    [1, 2, 4, NA],
    [NA, 33, 11, NA],
    [11, NA, NA, NA],
    [43, NA, NA, NA],
])
print(data2)

# thresh: value 갯수를 조건으로 가져오기
print(data2.dropna(thresh=2))


# 누락된 값을 채우기
# DataFrame에서는 누락된 데이터를 완벽하게 골라낼 수가 없으므로 다른 데이터도 함께 버려지게 된다.
# 이런 경우에는 fillna 메서드를 활용해서 NA를 채워주면 데이터의 손실을 막을 수 있다.
print(data2.fillna(0))

# fillna의 활용
# 각 칼럼마다 다른 값을 채워넣을 수 있다.
print(data2.fillna({
    1: 10,
    3: 30,
}))

# 보간법
print(data2)
print(data2.fillna(method='ffill', limit=1))  # limit는 보간 최대치를 설정

data3 = Series([1, NA, 4, NA, 7])
print(data3.fillna(data3.mean())) # 평균값으로 채우기