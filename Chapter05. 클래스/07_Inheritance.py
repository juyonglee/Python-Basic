# -*- coding: utf-8 -*

# 부모 클래스: 물려줄 클래스
# 자식 클래스: 물려받을 클래스
# 자식 클래스를 선언할 때는 클래스의 이름 뒤에 괄호()를 붙이고 그 안에 부모 클래스의 이름을 입력한다.
# Ex> class Child(Parent):

class Parent:
    def parent_method(self):
        print "parent_method"

class Child(Parent):
    def child_method(self):
        print "child_method"

parent = Parent()
parent.parent_method()

child  = Child()
# Parent로부터 물려받은 parent_method()를 소유하고 있다.
child.parent_method()

# OOP에서 상속의 중요한 특징 중 하나는 "자식 클래스의 객체를 부모 클래스의 객체로 간주한다"는 것입니다.
# 이러한 특징 때문에 객체 지향 프로그래밍을 기반으로 만들어진 코드는 업그레이드가 비교적 용이한 편이다.
class ArmorSuite:
    def armor(self):
        print "Armored!!"

class IronMan(ArmorSuite):

    pass

def get_armored(suite):
    suite.armor()

suite = ArmorSuite()
get_armored(suite)
iron_man = IronMan()
get_armored(iron_man)

# Python 2.X에서는 Old-Style class로 할 경우 type 에러가 발생하기 때문에
# class A(object)와 같은 형식으로 명시해 주어야 한다.
class A(object):
    def __init__(self):
        print "A.__init__()"
        self.message = "Made In A Class"

class B(A):
    def __init__(self):
        # B클래스에서 A클래스의 __init__()메소드를 호출 안할시 message 속성 접근 불가! 
        # A.__init__(self)
        # A.__init__(self) 대신 부모의 __init__()을 호출하는 super를 정의하여 사용
        # But, 부모 클래스를 변경할 시 모든 코드를 수정해야 한다.
        # 이를 해결하기 위해 08_Super.py에서 super() 함수에 대해 자세히 설명하겠습니다.
        super(B, self).__init__()
        print "B.__init__()"

obj = B()
print obj.message