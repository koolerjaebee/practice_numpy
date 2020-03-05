import pandas as pd
from pandas import Series, DataFrame

data = {
    'Seoul': 4000,
    'Busan': 2000,
    'Incheon': 1500,
    'Kwangju': 1000,
}

obj = Series(data)
print(obj)

cities = ['Seoul', 'Daegu', 'Incheon', 'Kwangju']
obj2 = Series(data, index=cities)
print(obj2)

print(obj + obj2)  # 없는 데이터가 하나라도 있으면 NaN이 나옴

# Series 객체(ex: obj, obj2)와 Series의 색인(index)은 모두 name라는 속성이 있다.

obj2.name='인구 수'
print(obj2)

obj2.index.name = '도시'
print(obj2)

obj2.index=['Daejeon', 'Busan', 'Jaeju', 'Jeonju']
print(obj2)