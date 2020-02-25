import numpy as np

# 파이썬의 리스트를 사용하는 방법: array()
list1 = [1, 2, 3, 4]

a = np.array(list1)
print(a)
print(a.shape)

b = np.array([[1, 2, 3],[4, 5, 6]])
print(b)
print(b.shape)

print(b[0, 0])

print('-'*50)
# numpy에서 제공하는 함수를 사용하는 방법
# 배열에 모두 0을 집어 넣음: zeros()
# 모두 1을 집어넣음: ones()
# 사용자가 지정한 값을 넣음: full()
# 대각선으로는 1 나머지 0: eye()
aa = np.zeros((2, 2))
print(aa, type(aa))

aa = np.ones((2, 3))
print(aa)

aa = np.full((2, 3), 10)
print(aa)

aa = np.eye(4)
print(aa)

aa = np.array(range(20)).reshape((5, 4))  # reshape(): 다차원으로 변형하는 함수
print(aa)
