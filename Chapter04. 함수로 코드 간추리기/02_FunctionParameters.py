# -*- coding: utf-8 -*

# 매개변수
# 매개변수는 중간에서 둘 사이의 관계를 맺어주는 것을 의미한다.
# 즉, 호출자와 함수 사이의 관계를 맺어주는 변수를 뜻한다.
# 매개변수의 이름은 보통의 변수처럼 문자와 숫자와 _로 만들어 진다.
# 숫자가 이름 가장 앞에 오면 에러가 발생한다.
# 함수의 매개변수에는 어떤 자료형이든 사용할 수 있다.
print "<매개변수가 1개인 경우>"
def myABS(value):
    if value < 0:
        return -value
    else:
        return value

print myABS(-5)
print myABS(5)

print "<매개변수가 2개인 경우>"
def introduceFunc(name, university):
    print "My name is {0} in {1}.".format(name, university)
introduceFunc("JuYong Lee", "SangMyung University")

# 기본값 매개변수(Default Argument Value)
# 매개변수를 입력하지 않을 경우 기본값으로 할당하는 것
# 기본값 매개변수를 사용하려면 매개변수를 적용할 때 값을 할당해 놓으면 된다.
print "<기본값 매개변수>"
def inventFunc(event, limit=20):
    print "{0} 이벤트는 {1}명을 당첨자로 선정합니다.".format(event, limit)
inventFunc("Smart OS 출시기념")
inventFunc("IoT 기기 출시기념", 100)
# 호출자가 매개변수의 이름을 일일이 지정해 데이터를 입력하는 것도 가능하다
print "<개인정보>"
def personnel(name, position, nationality="Korea"):
    print "이름: {0}".format(name)
    print "직급: {0}".format(position)
    print "국적: {0}".format(nationality)
personnel(name="JuYong Lee", position="Ph.D Candidate")

# 가변 매개변수(Arbitrary Argument List)
# 매개변수 앞에 *를 붙여서 가변으로 지정한다.
# def 함수이름(*매개변수):
#     Code Block
# *를 이용하여 정의된 가변 매개변수는 Tuple이다.
# *일 경우 Tuple, **경우 Dictionary Type이다.
print "<*인 경우>"
def mergeString(*string_list):
    completeStr = ""
    for str in string_list:
        completeStr += str
    print completeStr
mergeString("안녕하세요~","여러분!")

print "<**인 경우>"
def print_team(**players):
    for key in players:
        print "Number: {0}, Name: {1}".format(key, players[key])
print_team(_1="Ronaldo", _2="Messi", _3="Ji-Sung Park")

# 주의!!
# 일반 매개변수 & 가변 매개변수
# 정의 순섬에 따라 호출방식이 달라진다.
# Case1. 가변 매개변수의 앞에 정의되어 있는 일반 매개변수
# 일반 매개변수 만 사용 가능
# Keyword 매개변수 사용 불가
# Case2. 가변 매개변수의 뒤에 정의되어 있는 일반 매개변수
# 일반 매개변수 사용 불가
# Keyword 매개변수 만 사용 가능
print "<Case1. 가변 매개변수의 앞에 정의되어 있는 일반 매개변수>"
def argumentOrder01(data, *dataList):
    print "First Argument is " + data
    for item in dataList:
        print "Arbitrary Argument List item is " + item
argumentOrder01("JuYong Lee", "juyonglee0208@gmail.com", "goal0208@naver.com")
# Error발생 - 매개변수 길이의 유추가 가능하기 때문에 Keyword 사용 금지
# argumentOrder01(data1 = "JuYong Lee", "juyonglee0208@gmail.com", "goal0208@naver.com")

print "<Case2. 가변 매개변수의 뒤에 정의되어 있는 일반 매개변수>"
def argumentOrder02(*dataList, data):
    print "First Argument is " + data1
    for item in dataList:
        print "Arbitrary Argument List item is " + item
# argumentOrder02("juyonglee0208@gmail.com", "goal0208@naver.com", data1="JuYong Lee")
# Error발생 - 매개변수 길이의 유추가 불가능하기 때문에 Keyword 사용
# argumentOrder02("juyonglee0208@gmail.com", "goal0208@naver.com", "JuYong Lee")