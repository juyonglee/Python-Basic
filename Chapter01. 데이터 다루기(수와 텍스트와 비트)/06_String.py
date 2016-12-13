# -*- coding: utf-8 -*-

# Python에서는 문자열을 다루는 자료형으로 string을 제공
# Python에서는 문자열을 ' 또는 " 로 감싸서 표현
# 여러 줄로 이루어진 문자열은 ''' 또는 """의 쌍으로 텍스트를 감싸서 표현 
greeting = 'Hello World'
print greeting

greeting = "Hello World"
print greeting

greeting = '''Hello World'''
print greeting

greeting = '''Hello, 
JuYong 
Lee 
World!'''
print greeting
print type(greeting)

greeting = """Hello, 
JuYong Lee 
World!"""
print greeting
print type(greeting)

# + 연산자가 문자열을 결합
print "My Name is " + "JuYong Lee."

# 문자열의 분리는 대괄호 연산자([])를 통해 수행
# 문자열의 일부를 분리해내는 것을 Slicing이라고 한다.
# 문자열의 처음부터 Slicing하기 원한다면 첫 번째 매개변수 생략
# 문자열의 마지막까지 Slicing하기 원한다면 두 번째 매개변수 생략
# 특정 위치에 있는 문자를 참조하고 싶을 때는 []사이에 index를 입력
data = "head********tail"
print data[4:12]
headData = data[:4]
print headData
tailData = data[12:]
print tailData
indexTest = "AbC"
print indexTest[1]

# in 연산자는 원하는 부분이 문자열 안에 존재하는지를 확인
# 문자열의 길이를 반환하는 함수 len()
name = "LeeJuYong"
boolVal = "Ju" in name
print boolVal
print len(name)

boolVal = "Jung" in name
print boolVal
