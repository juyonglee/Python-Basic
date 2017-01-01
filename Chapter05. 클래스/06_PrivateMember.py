# -*- coding: utf-8 -*

# class 안에서만 접근이 가능한 멤버를 일컬어 Private 멤버라고 한다.
# 안과 밖 모두에서 접근이 가능한 멤버는 Public 멤버라고 한다.
# private, public 등의 키워드를 이용하는 다른 프로그래밍 언어들과 다르게
# Python은 작명법(Naming)으로 둘을 구분한다.
# 두개의 밑줄 __이 접두사여야 한다. 
# Ex> __Name
# 접미사는 밑줄이 한 개까지만 허용된다. 
# Ex> __Name_
class HasPrivate:
    def __init__(self):
        self.public = "Public"
        # 접미사의 밑줄이 두 개 이상이면 Public 멤버로 간주한다.
        # Ex> __number__
        self.__private = "Private"
    def print_from_internal(self):
        print self.public
        print self.__private

obj = HasPrivate()
print "<Member에 직접 접근>"
print obj.public
# private 직접 접근 불가!
# print obj.__private
print "<Method 접근>"
obj.print_from_internal()

