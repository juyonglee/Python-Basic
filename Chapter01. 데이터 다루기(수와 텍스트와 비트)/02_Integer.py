# -*- coding: utf-8 -*-

# Python은 세 종류의 수를 지원
# 정수, 실수, 복소수

# 1. 정수
# Python에서는 메모리가 허용하는한, 무한대의 정수를 다룰 수 있다.
b = 1234567123456712345671234567123456712345671234567
print(b)
c = -1234567123456712345671234567123456712345671234567
print(c)

# 기존의 프로그래밍 언어와 비슷 But, / 과 //를 이해해야한다!!
result01 = 22/7
print(type(result01))
print(result01)
result02 = 22//7
print(type(result02))
print(result02)

# bin() - 숫자를 2진수로 변환한 텍스트를 반환
# oct() - 숫자를 8진수로 변환한 텍스트를 반환
# hex() - 숫자를 16진수로 변환한 텍스트를 반환
# 0b: 2진수, 0o: 8진수, 0x: 16진수
print("<2진수 표현>")
print(bin(10))
print("<2진수를 10진수로 표현>")
print(0b1010)

print("<8진수 표현>")
print(oct(16))
print("<8진수를 10진수로 표현>")
print(0o20)

print("<16진수 표현>")
print(hex(16))
print("<16진수를 10진수로 표현>")
print(0x10)

