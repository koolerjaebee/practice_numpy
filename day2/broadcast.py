import numpy as np

a = np.array([
    [1, 2],
    [3, 4],
])
b = 10

c = a * b
print(c)

x = np.array([
    [1, 2],
    [3, 4],
])
y = np.array([10, 20])
z = x * y
print(z)

x = np.array([
    [11, 21],
    [34, 43],
    [0, 9],
])
print(x)
print(x[0][1])

for row in x:
    print(row)

# 2차원 배열을 1차원 배열로 변환 (평탄화): flatten()
x = x.flatten()
print(x)

print(x[np.array([1, 3, 5])])

# x > 25 조건이 참인 원소만 꺼내옴.
print(x[x > 25])

# numpy 배열에 부등호 연산자를 사용한 결과는 bool 배열이다.
print(x > 25)