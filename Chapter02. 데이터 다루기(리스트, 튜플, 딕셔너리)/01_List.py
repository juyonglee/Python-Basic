# -*- coding: utf-8 -*-

# list
# 데이터의 목록을 다루는 자료형
# 개별 데이터를 일컬어 요소(Element)라고 한다.
# 리스트를 만들 때 []를 사용한다.
# 리스트에는 어떤 데이터든 넣을 수 있다.
laboratory = ["I605-A", "I605-B", "I606-A", "I606-B"]
print laboratory[1]
print "SangMyung University Laboratory Lab [{0}]".format(laboratory[1])

# 리스트도 순서를 가지므로 문자열처럼 Slicing이 가능하다
location = laboratory[1:3]
print location[0]
print location[1]

# + 연산자를 이용하여 리스트간의 결합이 가능하다.
# len을 이용하여 길이를 측정한다.
firstName = ["JuYong"]
lastName = ["Lee"]
name = firstName + lastName
print len(name)
print name
print "My name is {0} {1}".format(name[0], name[1])
