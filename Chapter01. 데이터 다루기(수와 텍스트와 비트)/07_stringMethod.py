# -*- coding: utf-8 -*-

# 문자열은 다양한 기능의 함수를 탑재하고 있다.
# 특정 자료형이 갖고 있는 함수를 method라고 한다.

# startswith() - 입력한 문자열로 시작되는지
# endswith() - 입력한 문자열로 끝나는지
print "<startswith() & endswith()>"
print "LeeJuYong".startswith("Lee")
print "LeeJuYong".endswith("Lee")

# find() - 입력한 문자열이 존재하는 위치를 검색
# rfind() - 입력한 문자열이 존재하는 위치를 역으로 검색
# 입력한 문자열이 존재하지 않으면 -1을 return한다.
print "<find() & rfind()>"
print "LeeJuYong".find("x")
print "LeeJuYong".find("J")
print "LeeJuYong".rfind("J")

# lstrip() - 왼편의 공백을 제거 
# rstrip() - 오른편의 공백을 제거
# strip() - 양쪽의 공백을 제거
print "<lstrip() & rstrip() & strip()>"
print "     Lee JuYong".lstrip()
print "Lee JuYong     ".rstrip()
print "    Lee JuYong     ".strip()

# isalnum() - 문자열이 알파벳과 숫자로만 이루어져 있는지를 평가
print "<isalnum()>"
print "01094**1111".isalnum()
print "0109472".isalnum()

# replace() - 문자열에서 찾고자 하는 문자열을 바꾸고자 하는 문자열고 변경한다.
print "<replace()>"
print "YouJuYong".replace("You", "Lee")

# split() - 매개변수로 입력한 문자열을 문자열을 나눠 리스트를 만든다.
phoneOS = "Android, Window, Linux, iOS"
eachOS = phoneOS.split(", ")
print eachOS[3]

# upper() - 원본 문자열을 모두 대문자로 변경
# lowwer() - 원본 문자열을 모두 소문자로 변경
stringData = "ABC"
lowerString = stringData.lower() 
print lowerString
print lowerString.upper()

# format() - 형식을 갖춘 문자열을 만들 때 사용 {}로 다른 데이터가 들어갈 자리를 만들어두고 
# format 함수를 호출할 때 이 자리에 들어갈 데이터를 순서대로 넣어주면 된다.
greeting = "My name is {0}. I am a {1}"
print greeting.format("LeeJuYong", "Ph.D Candidate.")

# 생성자 
# int의 생성자: int()
# float의 생성자: float()
# complex의 생성자: complex()
# str의 생성자: str()
print "1st 입력"
input01 = input()
print "2nd 입력"
input02 = input()
# input으로 입력받은 내용은 문자열이므로 아래와 같이 연산이 불가능 
# 생성자를 이용하여 해결해야한다
# result = input01 * input02
result = int(input01) * int(input02)
message = "{0} x {1} = {2}"
print message.format(input01, input02, result)