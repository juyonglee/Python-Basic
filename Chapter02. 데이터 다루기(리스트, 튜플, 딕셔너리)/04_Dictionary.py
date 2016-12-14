# -*- coding: utf-8 -*-

# Dictionary 
# 사용법 측면에서는 리스트와 비슷
# 리스트는 요소에 접근할 때 인덱스를 사용해야만 한다. Ex> dic[0]
# Dictionary는 문자열과 숫자를 비롯해서 변경이 불가능한 형식이면 어떤 자료형이든 사용할 수 있다.
# Key - Value 방식을 사용한다.
# 탐색속도가 빠르고, 사용하기 편리하다.
# Dictionary는 키를 이용해서 단번에 데이터가 저장된 위치의 주소를 계산해내기 때문이다. (Hashing을 이용)
# 즉, 키를 Hashng해서 주소를 계산하기 때문이다.
# Dictionary를 만들 때는 {}를 이용한다.
print "<Dictionary>"
dic = {}
dic["Naver"] = "www.naver.com"
dic["Google"] = "www.google.com"
dic["Daum"] = "www.daum.net"

print dic["Naver"]
print type(dic)
print dic

# Dictionary가 제공하는 Method
# keys(): 키의 목록을 반환
# values(): 값의 목록을 반환
# items: Key-Value의 쌍으로 이루어진 전체 목록을 반환
# in: 특정 키가 키 목록 안에 존재하는지를 확인할 수 있다. or 특정 값이 값 목록 안에 존재하는지를 확인할 수 있다.
# pop: Dictionary에 존재하는 값을 제거할때 사용 (매개변수로 Key-Value를 전달)
# clear: Dictionary의 데이터를 모두 삭제 
print "\n<Dictionary가 제공하는 Method>"
print "<keys()>"
print dic.keys()

print "\n<values()>"
print dic.values()

print "\n<items()>"
print dic.items()

print "\n<in 연산자>"
print "Apple" in dic.keys()
print "Naver" in dic.keys()
print "www.naver.com" in dic.values()
print ("Google", "www.google.com") in dic.items()

print "\n<pop()>"
print "Before pop(): {0}".format(dic)
# dic.pop("Daum")도 가능
dic.pop("Daum", "www.daum.net")
print "After pop(): {0}".format(dic)

print "\n<clear()>"
print "Before clear(): {0}".format(dic)
dic.clear()
print "After clear(): {0}".format(dic)