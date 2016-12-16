# -*- coding: utf-8 -*-
import sys
# Code Block과 들여쓰기
# 대부분의 프로그래밍 언어들이 {}를 이용하여 Code Block을 표현
# 주의!!! Python은 들여쓰기로 구역을 나눈다!!
# Python의 PEP(Python Enhancement Proposals)에서 스페이스 4칸을 사용할 것을 추전
# 주의!!! 들여쓰기를 무작정 시작하면 안 된다!! 시작 전 윗줄에 :을 위치시켜야 한다.

# if문 
# if 뒤에 흐름을 가를 조건이 위치하고, 그 뒤에 :을 위치시킨다.
# Code Block을 위치시키기 위해서 :을 붙여준다.
# if절의 조건이 거짓일때 else절로 코드가 간다.
value = 30
if value == 30:
    print "value is 30."
else:
    print "value is not 30."

if value <= 20:
    print "value is less than 20 or same 20."
else:
    print "value is more than 20."

print "\n<3/입력 나눗셈 기능>"
print "수를 입력하세요: "
a = float(input())
if a==0:
    print "0은 나눗셈에 이용할 수 없습니다."
else:
    print "====================="
    print "3/{0}의 몫은 {1}입니다.".format(a, 3/a)

# exit()함수를 사용하기 위해 sys패키지를 import해야한다.
print "\n<exit()>"
print "값을 입력하세요: "
input = int(input())
if input >= 100:
    print "100 이상은 입력하실 수 없습니다."
    print "프로그램이 종료됩니다."
    sys.exit();
else:
    print "100 이하의 수를 입력하셨습니다."

# elif
# Python에서 여러 조건을 생각해야 하는 경우 if와 함께 elif를 사용한다.
# else if를 줄여서 만든 Python Keyword입니다.
print "\n<학점 산출 프로그램>"
print "학생의 점수를 입력하세요: "
score = int(input)
if score > 90:
    print "학점 A+"
elif score > 80:
    print "학점 B+"
else:
    print "재수강"

# 중첩 if문
print "\n<중첩 if문>"
valueCheck = 20

if valueCheck >= 20:
    if valueCheck%2 == 0:
        print "20이상의 짝수입니다."
    else:
        print "20이상의 홀수입니다."
else:
    if valueCheck%2 == 0:
        print "20미만의 짝수입니다."
    else:
        print "20미만의 홀수입니다."

# 여러 조건을 평가할 때, 중첩 if문 대신 and & or 연산자를 이용하는 것도 좋은 방법이다.
print "\n<연산자 이용 예제>"
if valueCheck >= 20 and valueCheck%2 == 0:
    print "20이상의 짝수입니다."
elif valueCheck >= 20 and valueCheck%2 != 0:
    print "20이상의 홀수입니다."
elif valueCheck < 20 and valueCheck%2 == 0:
    print "20미만의 짝수입니다."
else:
    print "20미만의 홀수입니다."
