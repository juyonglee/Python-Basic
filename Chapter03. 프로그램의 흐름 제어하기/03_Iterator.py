# -*- coding: utf-8 -*-

# 반복문
# while, for

print "<반복문>"
# while 조건: Code Block
print "1. while"
print "몇 번 반복하시겠습니까?"
startVal = 1
repeatVal = int(input())
while startVal <= repeatVal:
    print "{0}번째 반복!".format(startVal);
    startVal += 1

# for 반복변수 in 순서열: Code Block
# 순서열에는 List, Tuple, 문자열 등을 사용할 수 있다.
print "\n2. for"
soccerPlayer = ["박지성", "이동국", "박주영", "메시", "호날두"]
print "<Soccer Player>"
for item in soccerPlayer:
    print item

print "<한글 Index>"
koreanList = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ"]
for char in koreanList:
    print char

# range 함수는 연속하는 두 수의 차이가 일정한 수열을 의미한다.
# for 변수 in range(시작값, 멈춤값, 연속하는 두수의 차)
print "<두수의 차가 1인경우>"
for i in range(0, 5, 1):
    print "변수 i의 값은 {0}입니다.".format(i)
print "<두수의 차가 2인경우>"
for i in range(0, 5, 2):
    print "변수 i의 값은 {0}입니다.".format(i)
# 두수의 차는 생략이 가능하다.
# 생략하면 range()는 두수의 차를 1로 간주한다.
print "<두수의 차를 생략한 경우>"
for i in range(0, 5):
    print "변수 i의 값은 {0}입니다.".format(i)
# 멈춤값만 입력해서 호출할 수도 있다.
# 이러한 경우 시작값은 0, ㅇ녀속하는 두수의 차를 1로 간주한다.
print "<멈춤값만 입력한 경우>"
for i in range(5):
    print "변수 i의 값은 {0}입니다.".format(i)

for i in range(1, 10):
    print "<{0}단>".format(i)
    for j in range(1, 10):
        print "{0}x{1}={2}".format(i, j, i*j)

for i in range(1, 6):
    for j in range(i):
        # print "", 작성하면 줄바꿈 문자가 제거된다.
        print "*",
    print ""

print "<Dictionary Tuple Unpacking 방식>"
dic = {"애플": "www.apple.com", "마이크로소프트": "www.microsoft.com", "파이썬": "www.python.org"}
for K, V in dic.items():
    print "{0}의 홈페이지 주소는 {1}입니다.".format(K, V)

# continue와 break로 반복문 제어하기
# continue는 반복문이 실행하는 Code Block의 나머지 부분을 실행하지 않고 다음 반복으로 넘어간다
# break는 반복문을 중단시키는 기능을 한다.
print "\n<continue와 break>"
print "1. continue"
for i in range(1, 11):
    if i%2 == True:
        continue
        print "실행이 될까?"
    print "짝수: {0}".format(i)

print "2. break"
for i in range(2000):
    if i>1000:
        print "i가 {0}이 넘었습니다. 반복문을 중단합니다.".format(i-1)
        break;