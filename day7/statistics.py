# 기술 통계 계산

# pandas는 일반적인 수학/통계 메서드를 가지고 있다.
# pandas의 메서드는 처음부터 누락된 데이터를 제외하도록 설계되어 있다.

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

df = DataFrame(
    [
        [1.4, np.nan],
        [7.1, -4.5],
        [np.nan, np.nan],
        [0.75, -1.3],
    ],
    index=['a', 'b', 'c', 'd'],
    columns=['one', 'two'],
)
print(df)

# sum() 메서드는 각 칼럼의 합을 더해서 Serires 객체를 반환한다.
print(df.sum())
print(df.sum(axis=1))  # 각 행의 합을 반환한다.

# 전체 행이나 column의 값이 NaN이 아니라면 NaN 값은 제외시키고 계산을 하는데
# skipna옵션은 전체 row나 column의 값이 NaN이 아니라도 제외시키지 않을 수 있다.
# skipna의 default는 True
print(df.sum(axis=1, skipna=False))  # 하나라도 NaN이 있으면 계산 x


# idxmin, idxmax와 같은 ㅅ메서드는 최소, 최댓값을 가지고 있는 색인 값 같은 간접 통계를 반환한다.
print(df.idxmax())
print(df.idxmin())


# 누산 메서드: cumsum()
print(df.cumsum())


# 유일한 값, 도수 메서드
s1 = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
unique = s1.unique()
print(unique)  # 중복된 값을 없애는 메서드
print(unique.sort())  # sort 못함

cnt = s1.value_counts()  # 값의 수를 계산(도수), 반환값은 Series 객체
print(cnt)  # 내림차순으로 정렬되며 같은 값은 먼저 나온 순서


# isin 메서드는 어떤 값이 Series에 있는지 나타내는 메서드
# boolean 값(Treu, False)을 반환한다.
# DataFrame, Series에서 원하는 값을 골라내고 싶을 때 유용하게 사용하는 메서드
mask = s1.isin(['b', 'c'])
print(mask)  # b 또는 c 가 있으면 true값 반환
print(s1[mask])  # mask를 씌워 원하는 값만 보여주는 것으로 활용 가능

data = DataFrame(
    {
        'Q1': [1, 3, 4, 3, 4],
        'Q2': [2, 3, 1, 2, 3],
        'Q3': [1, 5, 2, 4, 4],
    }
)
print(data)

# unique 값들을 가져와서 count 함 그리고 그걸 다시 DataFrame화
res = data.apply(pd.value_counts)
print(res)
res = data.apply(pd.value_counts).fillna(0)
print(res)


# 누락된 데이터 처리(pandas의 설계 목표 중 하나는 누락된 데이터를 쉽게 처리하는 것)
# pandas 에서는 누락된 데이터를 실수든 아니든 모두 NaN(Not a Numver)으로 취급한다.
stringData = Series(['aaa', 'bbbb', np.nan, 'ccccc'])
print(stringData)

# 이러한 NaN의 값은 파이썬의 None값 NA(Not Available)와 같은 값으로 취급한다.
print(stringData.isnull())

stringData[0] = None
print(stringData)
print(stringData.isnull())