# -*- coding: utf-8 -*-

# 실수(Real Number)를 지원하기 위해 부동 소수형을 제공
# 부동 소수형은 8바이트만을 이용해서 수를 표현하기 때문에 한정된 범위만 표현가능
# 정밀도의 한계를 가진다.

a = 3.14
print(a)

# b는 무리수이다. 하지만 부동 소수형에서는 표현이 가능하므로 오차가 발생
b = 22/10.0
print(b)

result = a + b
print(result)
result = a / b
print(result)
result = a // b
print(result)

# 부동 소수형이기 때문에 0.10000000000000142이 출력된다.
result = 43.2 - 43.1
print(result)