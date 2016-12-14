# -*- coding: utf-8 -*-

# Immutable Type vs Mutable Type
# Immutable은 변경이 불가능한 자료형이며 Mutable Type에 비해 
# 소프트웨어의 성능을 향상하는데 도움을 준다.
# 데이터를 할당할 공간의 내용이나 크기가 달라지지 않기 때문에 생성 과정이 간단
# 또한 수정이 필요 없으므로 복사본이 아닌 원본을 사용하므로 성능이 좋음
# 문자열 또한 변경이 불가능한 자료형이다.

# Tuple
# 리스트의 요소는 변경이 가능하지만 Tuple은 요소 변경이 불가능하다
# 리스트는 목록 형식의 데이터를 다루는데 적합, Tuple은 작은 규모의 자료 구조를 구성하기 좋다
# ()를 이용하여 Tuple을 생성한다
print "\n<Tuple 정의>"
httpCode = (80, "Success")
print "HTTP Code: {0}".format(httpCode[0])
print "HTTP Message: {0}".format(httpCode[1])
print type(httpCode)

# 주의 요소가 하나뿐인 Tuple을 정의할 떄는 요소 뒤에 콤마(,)를 반드시 넣어줘야 합니다.
print "\n<요소가 하나뿐인 Tuple정의>"
myCode01 = (4097)
print myCode01
print type(myCode01)
myCode02 = (4097, )
print myCode02
print type(myCode02)

# 튜플도 리스트와 문자열처럼 순서열 자료형이다
# 참조 연산과 슬라이싱 Tuple간 결합 등이 가능하다
print "\n<Tuple간 결합>"
numberList = (1, 2, 3, 4, 5, 6)
print numberList[1:3]
print numberList[ :3]
numberList += (7, 8, 9, 10)
print numberList
print numberList[6:9]

# 문자열,리스트와 마찬가지로 len()함수를 이용하여 Tuple의 길이를 반환
print "\n<len()함수를 이용한 Tuple길이>"
print "Tuple numberList의 길이는 {0}입니다.".format(len(numberList))

# Tuple Packing & Tuple Unpacking
# 여러가지 데이터를 Tuple로 묶는 것을 Tuple Packing이라고 한다.
# Tuple의 각 요소를 여개 개의 변수에 할당하는 것을 Tuple Unpacking이라고 한다.
# Tuple Unpacking 할 때는 Tuple 요소의 수와 각 요소를 담아낼 변수의 수가 일치해야한다.
print "\n<Tuple Packing>"
http = 404, "Page Not Found"
print http

print "\n<Tuple Unpacking>"
code, message = http
print "Error Code: {0}, Error Message: {1}!".format(code, message)

# Tuple Method
# 제공하는 메소드는 index()와 count() 두 개뿐이다.
print "\n<Tuple Method>"
numbers = (1, 3, 6, 7, 20, 20, 38, 20)
print "numbers Tuple 요소의 값이 20인 요소의 index는 {0}입니다.".format(numbers.index(20))
print "numbers Tuple 요소의 값이 20인 요소의 개수는 {0}개 입니다.".format(numbers.count(20))