# -*- coding: utf-8 -*

# 정적 메소드(Static Method)는 데코레이터로 수식하며, self 매개변수 없이 정의합니다.
# 정적 메소드는 self 매개변수를 전달받을 방법이 없으므로 객체/인스턴스의 변수에 접근할 수 없습니다.
# 따라서 정적 메소드는 객체의 데이터 속성과는 관계가 없는 코드로 구현되는 것이 일반적입니다.
class Calculator:
    @staticmethod
    def plus(a, b):
        return a+b
    
    @staticmethod
    def minus(a, b):
        return a-b
    
    @staticmethod
    def multiply(a, b):
        return a*b
    
    @staticmethod
    def divide(a, b):
        return a/b
    
    @staticmethod
    def mod(a, b):
        return a%b

# 인스턴스를 통해서도 접근이 가능하지만 Class를 통해 호출하는 것이 보통이다.
print "{0} + {1} = {2}".format(3, 4, Calculator.plus(3, 4))
print "{0} - {1} = {2}".format(3, 4, Calculator.minus(3, 4))
print "{0} * {1} = {2}".format(3, 4, Calculator.multiply(3, 4))
print "{0} / {1} = {2}".format(3, 4, Calculator.divide(3, 4))
print "{0} mod {1} = {2}".format(3, 4, Calculator.mod(3, 4))