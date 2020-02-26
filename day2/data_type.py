import numpy as np

# int, float, bool(True / False), complex

# - int8(-128, 127), int16(-32768, 32767) (부호가 있는 정수형)
# uint(Unsigned integer): uint8(0 ~ 255), unit16(0, 65535), unit32, unit64

# 실수형(float)
# float16, float32, float64

# complex
# complex64: 두개의 32비트 부동소수점으로 표시되는 복소수
# complex128: 두개의 64비트 부동소수점으로 표시되는 복소수

# 데이터의 type을 알아보기위한 dtype

x = np.float32(1.0)

print(x)

print(type(x))

print(x.dtype)

z = np.arange(5, dtype='f')
print(z)

aa = np.array([1, 2, 3], dtype='f')
print(aa)
print(aa.dtype)

xx = np.int8(aa)
print(xx)
print(xx.dtype)

bb = np.arange(10)
print(bb)

cc = np.arange(3, 10, dtype=np.float)
print(cc)
print(cc.dtype)

dd = np.arange(2, 3, 0.1)
print(dd)