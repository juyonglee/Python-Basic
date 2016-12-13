# -*- coding: utf-8 -*-

# 여러 가지 수학 함수를 담고 있는 math 모듈이 존재
# math 모듈을 사용하기 위해서는 import를 해야 한다.
# abs(), round()는 Python 내장함수이다. 
# But, trunc는 math 모듈에 존재하는 함수이므로 math 모듈을 import한 뒤 사용해야한다.
import math

# 원주율 출력
print "<원주율 출력>"
print math.pi

# 자연상수(e) 출력
print "<자연상수 출력>"
print math.e

# 절대값, 버림과 반올림
print "<절대값 출력>"
print abs(10)
print abs(-10)

print "<버림 출력>"
print math.trunc(3.5)
print "<반올림 출력>"
print round(3.2)
print round(-3.5)

# Factorial 함수는 정수를 매개변수로 받는다.
# ex> 6! = 720
print "<팩토리얼 출력>"
print 6 * 5 * 4 * 3 * 2 * 1
print math.factorial(6)

# 도(Degree)와 라디안(Radian)
# Degree: 원을 360도로 표현한 것
# degrees() - 라디안을 입력받아 도를 계산
# Radian: 반지름이 1인 원에서 호의 길이가 1인 부채꼴의 각을 기본 삼아서 2PI로 표현한 것 (360 = 2PI)
# radians() - 도를 입력받아 라디안을 계산
print math.degrees(20)
print math.radians(360)

# 삼각함수
# a***():***()의 역함수
print math.sin(math.radians(30))
print math.sin(math.radians(45))
print math.sin(math.radians(60))
print math.sin(math.radians(90))

# 제곱과 제곱근
print "<제곱 출력>"
print 3 ** 3
print math.pow(3, 2)

print "<제곱근 출력>"
print math.sqrt(4)
a = 27 * (1.0/3)
print math.pow(a, 2)

# 로그
print "<밑수가 10인 로그>"
print math.log10(10 ** 10)
print "<밑수가 자연수 e인 로그>"
print math.log(math.e)