# -*- coding: utf-8 -*

# 호출자에게 반환하기
# 함수가 호출자에게 값을 반환할 경우 return문이 이용됩니다.
# 가급적이면 return문은 함수 Code Block의 마지막에 하나만 실행하도록 하는 것이 좋다.
print "<호출자에게 반환하기>"

def my_abs(arg):
    if arg < 0:
        return -arg
    elif arg > 0:
        return arg
print "1. 10의 절대값은 {0}입니다.".format(my_abs(10))
print "2. -10의 절대값은 {0}입니다.".format(my_abs(-10))
# 매개변수로 0을 입력받으면 아무것도 반환하지 않은 채로 실행을 종료한다.
# 이런 함수는 호출자에게 NoneType의 None을 반환
print "3. 0의 절대값은 {0}입니다.".format(my_abs(0))

print "\n<반복적인 문자열 출력>"
def repeatFunc(count):
    for i in range(0, count, 1):
        if i == 5:
            return
        print "Hello, World!"
print "몇번을 반복할까요?",
count = int(input())
repeatFunc(count)

print "\n<가변 문자열 출력>"
def print_something(*arg):
    for i in arg:
        print i,
print_something(0, 1, 0, "-", 1, 2, 3, 4, "-", 5, 6, 7, 8)