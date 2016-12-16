# -*- coding: utf-8 -*-

# bool 자료형
# True와 False 두 가지 값을 나타내는 자료형 
# 객체가 True 또는 False로 평가되는지를 알고 싶은 때틑 bool()함수를 이용한다.
boolTest = 3 > 2
print boolTest
boolTest = 3 < 2
print boolTest
print "boolTest Type: {0}".format(type(boolTest))

# 논리 연산자 (not, and, or)
# not 
# False인 경우 True, True인 경우 False
# 비어있는 문자열이나 Tuple, List, Dictionary 모두 False로 간주
# None도 거짓으로 간주
print "\n<논리 연산자>"
print "1. not 연산자"
print "None은 기본적으로 {0}로 간주!".format(bool(None))
strValue = ""
print "내용이 없는 문자열인 경우: {}".format(bool(strValue))
strValue = "JuYong Lee"
print "내용이 있는 문자열인 경우: {0}".format(bool(strValue))
tupleValue = ()
print "내용이 없는 Tuple인 경우: {0}".format(bool(tupleValue))
tupleValue = (200, "Success")
print "내용이 있는 Tuple인 경우: {0}".format(bool(tupleValue))
dicValue = {};
print "내용이 없는 Dictionary인 경우: {0}".format(bool(dicValue))
dicValue["Google"] = "www.google.com"
print "내용이 있는 Dictionary인 경우: {0}".format(bool(dicValue))

# and: 논리곱을 수행
# 두 피연산자가 모두 True인 경우에만 True
print "2. and 연산자"
print "True and True: {0}".format(True and True)
print "True and False: {0}".format(True and False)

# or: 논리합을 수행 
# 두 피연산자가 모두 False인 경우에만 False
print "3. or 연산자"
print "True or True: {0}".format(True or True)
print "True or False: {0}".format(True or False)
print "False or False: {0}".format(False or False)

# 비교 연산자(==, !=, >, >=, <, <=)
# ==
print "\n<비교 연산자>"
print "1. == 연산자"
value = 30
print "value is 30? {0}".format(value == 30)
print "value is 20? {0}".format(value == 20)

print "2. != 연산자"
print "value is not 20? {0}".format(value != 20)
print "value is not 30? {0}".format(value != 30)

print "3. > 연산자"
print "value is more than 20? {0}".format(value > 20)
print "value is more than 30? {0}".format(value > 30)

print "4. >= 연산자"
print "value is more than 20 or same 20? {0}".format(value >= 20)
print "value is more than 30 or same 30? {0}".format(value >= 30)

print "5. < 연산자"
print "value is less than 20? {0}".format(value < 20)
print "value is less than 30? {0}".format(value < 30)

print "6. <= 연산자"
print "value is less than 20 or same 20? {0}".format(value <= 20)
print "value is less than 30 or same 30? {0}".format(value <= 30)