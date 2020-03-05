# pandas 자료구조 : Series, DataFrame

import pandas as pd
from pandas import Series, DataFrame

# Series는 일차원 배열 같은 자료구조

obj = Series([3, 22, 34, 11])
print(obj)
print(obj.values)
print(obj.index)

obj2 = Series([4, 5, 6, 2], index=['d', 'c', 'e', 'f'])
print(obj2)  # 지정 순서
print(obj2['c'])
print(obj2[['d', 'f', 'c']])
print(obj2*2)
print('b' in obj2)
print('c' in obj2)

data = {
    'kim': 3400,
    'hong': 2000,
    'kang': 1000,
    'lee': 2400,
}
obj3 = Series(data)
print(obj3)  # 오름차순

name = [
    'woo',
    'hong',
    'kang',
    'lee',
]
obj4 = Series(data, index=name)
print(obj4)  # NaN == Not a Number

# 누락된 데이터를 찾을 때 사용하는 함수 isnull, notnull

print(pd.isnull(obj4))

print(pd.notnull(obj4))