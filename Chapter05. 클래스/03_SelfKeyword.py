# -*- coding: utf-8 -*

# Python Method에 사용되는 self가 가리키는 '자신'은 무엇일까?
# Method가 소속되어 있는 Object이다.
class ContactInfo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

JuYongLee = ContactInfo("이주용", "juyonglee0208@gmail.com")
print "이름: {0}".format(JuYongLee.name)
print "이메일: {0}".format(JuYongLee.email)

# ContactInfo 외부에서는 JuYongLee라는 이름으로 객체를 다룰 수 있다.
# 하지만 ContactInfo 내부에서는 JuYongLee처럼 객체를 지칭할 수 있는 이름이 없다.
# 따라서 self를 도입한 것이다!!
# 왜 Python은 모든 메소드마다 self를 필수 객개변수로 입력받도록 했을까?
# C++, Java등에서는 this가 암묵적으로 정의되어 있어서 this 키워드를 입력할 필요가 없다.
# But, Python에서는 명시적으로 사용한다.