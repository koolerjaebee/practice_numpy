import numpy as np

br = '-' * 50

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# c = a + b
c = np.add(a, b)
print(c)

print(br)

# c = a - b
c = np.subtract(a, b)
print(c)

print(br)

# c = a * b
c = np.multiply(a, b)
print(c)

print(br)

c = a / b
c = np.divide(a, b)
print(c)

print(br)

ls1 = [
    [1, 2],
    [3, 4],
]

ls2 = [
    [5, 6],
    [7, 8],
]

a = np.array(ls1)
b = np.array(ls2)

# dot(): matrix 곱

print('두 matrix에 대한 product 구하기')

product = np.dot(a, b)

print(product)

# sum(): 각 요소의 합
# prod(): 각 요소의 곱
# 이 함수들은 axis 옵션을 사용, axis 0이면 열끼리, 1이면 행끼리

a = np.array([
    [1, 2],
    [3, 4],
])

s = np.sum(a)
print(s)

s = np.sum(a, axis=0)
print(s)

s = np.sum(a, axis=1)
print(s)

p = np.prod(a)
print(p)

p = np.prod(a, axis=0)
print(p)

p = np.prod(a, axis=1)
print(p)