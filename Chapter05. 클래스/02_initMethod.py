# -*- coding: utf-8 -*

# Class의 생성자가 호출되면 내부적으로 또 다른 두 개의 메소드가 호출된다.
# Magic or Special 메소드라고 불린다. (__로 싸여 있는 이름을 가지는 것이 특징이다.)
# __new__() 
# __init__()
# 생성자가 호출되면 가장 먼저 __new__() 메소드가 호출된다.
# __new__() 메소드의 역할은 Class의 Instance를 만드는 것이다.
# __new__() 메소드는 Class 메소드이기 때문에 Instance 속성에 접근하기 힘들다.
# __init__() 메소드는 Instance 메소드이기 때문에 Instance 변수를 다루기에 적합하다.
# 즉, __new__() : 객체 생성 담당, __init__() : 객체 초기화 담당

# Class 속성
# text_list는 Car Class의 정의 시점에 함께 메모리에 할당
# obj 객체가 생성되기 전부터 text_list가 메모리에 적재되어 있다.
class Player:
    playerList = []
    def addPlayer(self, player):
        self.playerList.append(player)
    def printList(self):
        print self.playerList

print "\n<Class Method>"
obj = Player()
print "<obj: Before Player List>"
obj.printList()
obj.addPlayer("Ronaldo")
obj.addPlayer("Messie")
print "<obj: After Player List>"
obj.printList()

print "<obj2: Before Player List>"
obj2 = Player()
obj2.printList()
print "<obj2: After Player List>"
obj.printList()
# Class Player의 모든 인스턴스가 공유하게 되어 생긴 문제!!

# Instance 속성
print "\n<Instance Method>"
class InstancePlayer:
    def __init__(self):
        self.playerList = []
    def addPlayer(self, player):
        self.playerList.append(player)
    def printList(self):
        print self.playerList

Team01 = InstancePlayer()
print "<Team01: Before Player List>"
Team01.printList()
Team01.addPlayer("박지성")
print "<Team01: After Player List>"
Team01.printList()

print "<Team02: Before Player List>"
Team02 = InstancePlayer()
Team02.printList()
Team02.addPlayer("이천수")
Team02.addPlayer("이근호")
print "<Team02: After Player List>"
Team02.printList()