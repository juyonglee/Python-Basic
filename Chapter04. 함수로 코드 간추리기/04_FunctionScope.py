# -*- coding: utf-8 -*

# 함수 밖의 변수, 함수 안의 변수
print "<함수 밖의 변수, 함수 안의 변수>"
# Scope
# 변수는 자신이 생성된 Code Block 안에서만 유효하다.
# 지역 변수(Local Variable)
# 함수 안에서 만든 변수는 함수 안에서만 살아있다가 함수 코드의 실행이 종료되면 그 생명을 다합니다. 
# 전역 변수(Global Variable)
# 전역 변수로 사용하려면 global keyword를 이용해야한다.
print "<Local Scope Example>"
port = 8080
def scope_test():
    port = 100
    print "scope_test function scope port value is {0}.".format(port)
scope_test()

print "\n<Global Scope Example>"
def scope_test02():
    global mysqlPort 
    mysqlPort = 3000
    print "scope_test02 function scope mysqlPort value is {0}.".format(mysqlPort)
scope_test02()
print "Global mysqlPort Value is {0}.".format(mysqlPort)
mysqlPort = 3306
print "Global mysqlPort Value is {0}.".format(mysqlPort)