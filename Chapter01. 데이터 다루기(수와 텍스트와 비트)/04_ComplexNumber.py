# -*- coding: utf-8 -*-
# 실수가 정수를 포함하는 것처럼 복소수도 실수를 포함
# 실수는 허수부가 0인 복소수
# Python에서 허수 단위를 나타내는 부호로는 i대신 j를 사용
# 복소수의 허수부(imag), 실수부(real), 켤레 복소수 출력법(conjugate)
a = 2 + 3j
print(type(a))
print(a.real)
print(a.imag)
print(a.conjugate())

print (1 + 5j) + (2 -2j)
print (1 + 2j) - (3 + 4j)
print (1 + 2j) * (3 + 4j)
print (1 + 2j) / (3 + 4j)
