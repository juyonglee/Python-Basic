# -*- coding: utf-8 -*

# Class 메소드는 Static 메소드처럼 Class Member이다.
# 정의할 때 @classmethod 데코레이터와 cls 매개변수가 필요하다.
# cls 매개변수는 Calculator Class를 나타낸다.

class TestClass:
    @classmethod
    def print_TestClass(cls):
        print cls

TestClass.print_TestClass()

obj = TestClass()
obj.print_TestClass()

# Class의 객체가 몇 개가 생성되었는지를 카운트하는 프로그램
class InstanceCount:
    count = 0
    def __init__(self):
        InstanceCount.count += 1
        print "{0}번째 Instance 생성!".format(InstanceCount.count)

    @classmethod
    def printInstanceCount(cls):
        print "생성된 Instance의 {0}개 입니다.".format(cls.count)
        print "=========================="

object01 = InstanceCount()
InstanceCount.printInstanceCount()

object02 = InstanceCount()
InstanceCount.printInstanceCount()

object03 = InstanceCount()
InstanceCount.printInstanceCount()