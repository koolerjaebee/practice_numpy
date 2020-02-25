# numpy 슬라이싱
import numpy as np

br = '-' * 50

ls1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

arr = np.array(ls1)

a = arr[0:2, 0:2]  # rank 순으로 slicing
print(a)

b = arr[1:, 1:]
print(b)

print(br)
# numpy 정수 인덱싱(integer indexing)
# numpy 배열 a에 대해서 a[[row1, row2], [col1, col2]]는
# a[row1, col1]과 a[row2, col2]라는 두개의 배열 요소 집합을 의미
ls2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

a = np.array(ls2)

# 정수 인덱싱
res = a[[0, 2], [1, 3]]  # 1대1 대응 요소들의 집합 ex) a[0][1] 과 a[2][3] 의 집합

print(res)

print(br)
# boolean 인덱싱
ls3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

aa = np.array(ls3)

b_arr = np.array([
    [False, True, False],
    [True, False, True],
    [False, True, False],
])

n = aa[b_arr]

print(n)

# 표현식 이용하기

ls4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

arr = np.array(ls4)

# 배열 a에 대해서 짝수인 배열 요소만 True로 지정
b_arr = (arr % 2 == 0)

# print(b_arr)
print(arr[b_arr])

n = arr[arr%2 == 0]
print(n)