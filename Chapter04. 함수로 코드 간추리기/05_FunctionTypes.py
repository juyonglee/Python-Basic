# -*- coding: utf-8 -*

# Recursive Function (재귀함수)
# 자기 스스로를 호출하는 함수를 의미
# 재기 함수는 재귀 관계식(Recurrence relation, 점화식)을 
# 코드로 옮기고자 할때 유용하다.
# 재귀 함수는 호출 비용이 크기때문에 가급적 반복문으로 대체하는 것이 좋다
# 주의!! 종료 조건을 적절하게 만들지 못할 경우 무한루프에 빠질 수 있다.

# n!
# 1 (n=0)
# n*(n-1)! (n>0)
print "<Fatorial Example>"
def factorial(n):
    if n > 0:
        result = n * factorial(n-1)
    elif n == 0:
        result = 1
    return result
print "3!의 결과는 {0}입니다.".format(factorial(3))
print "6!의 결과는 {0}입니다.".format(factorial(6))

# Python에서는 함수를 변수에 담아 사용이 가능하다
# 순서열이나 Dictionary에도 함수를 담을 수 있다.
print "\n<함수를 변수에 담아 사용하기>"
def helloFunction(name):
    print "Hello, " + name + "!"
greeting = helloFunction
greeting("JuYong Lee")
greeting("Ronaldo")

# Python은 함수를 First Class Object로 다루기 때문에 가능하다.
# First Class Object는 매개변수로 넘길 수 있고 함수가 반환할 수도 있다.
# 또한 변수에 할당이 가능하다.
def plus(a, b):
    return a+b
def minus(a, b):
    return a-b
def multiply(a, b):
    return a*b
calculator = [plus, minus, multiply]
print "10 + 30 = {0}".format(calculator[0](10, 30))
print "10 - 30 = {0}".format(calculator[1](10, 30))
print "10 * 30 = {0}".format(calculator[2](10, 30))

calcDictionary = {"Plus": plus, "Minus": minus, "Muliply": multiply}
print type(calcDictionary)
print "10 + 30 = {0}".format(calcDictionary["Plus"](10, 30))
print "10 - 30 = {0}".format(calcDictionary["Minus"](10, 30))
print "10 * 30 = {0}".format(calcDictionary["Muliply"](10, 30))

# Python에서는 함수를 다른 함수의 매개변수로 사용할 수 있다.
print "\n<함수를 다른 함수의 매개변수로 사용하는 예제>"
def helloKOR():
    print "안녕하세요!"
def helloENG():
    print "Hello!"

def helloPrint(hello):
    hello()
helloPrint(helloKOR)
helloPrint(helloENG)

def helloNameKOR(name):
    print "안녕하세요, " + name + "!"
def helloNameENG(name):
    print "Hello, " + name + "!"
def helloPrintName(hello, name):
    hello(name)
helloPrintName(helloNameKOR, "이주용")
helloPrintName(helloNameENG, "JuYong Lee")

print "\n<함수를 반환하는 예제>"
def helloLanguage(national):
    if national == "KOR":
        return helloKOR()
    elif national == "ENG":
        return helloENG()
helloLanguage("KOR")
helloLanguage("ENG")

# Python에서는 함수 안에 함수를 정의하는 것이 가능하다.
# 함수 안에 정의된 함수를 중첩함수(Nested Function)라고 한다.
# 중첩함수는 자신이 소속된 함수의 매개변수에 접근할 수 있다
print "\n<함수 안의 함수: 중첩함수>"
def nestedFunction(name, school):
    def printNameFunc(name):
        return "안녕하세요 " + name  + "입니다!"
    def printSchoolFunc(school):
        print printNameFunc(name) + "\n저의 학교는 " + school +"입니다."
    printSchoolFunc(school)

nestedFunction("이주용", "상명대학교")

# Pass
# pass keyword는 함수나 클래스의 구현을 미룰 때 사용한다.
# C/C++ 처럼 {}를 이용해서 코드블록을 구성하는 언어인 경우 빈 구현을 만드는데 아무 문제가 없지만
# Python처럼 들여쓰기를 이용하는 언어는 빈 구현을 만들려면 난감하기 짝이 없다
# 따라서 Python에서는 pass keyword를 이용하여 빈 구현을 만든다.
print "\n<Pass Keyword>"
def emptyFunc():
    pass
class emptyClass:
    pass