# -*- coding: utf-8 -*

# Object & Class
# Object = Attribute + Method
# Ex> 자동차 
# Attribute: Color, Wheel Size, Displacement
# Method: Foward, Backward, Turn Left, Turn Right
# Object = Attribute<변수> + Method<함수>

# Class를 만드는 법
# Class ClassName:
#     Code Block
# 주의!!! - Method와 Function의 차이
# Function: 일련의 코드를 하나의 이름으로 묶은 코드 요소
# Method: Class Member라는 점
class Car:
    # __init__() Method는 객체가 생성될 대 호출되며 객체의 초기화를 담당
    # Python이 Dynamic한 언어이기 때문에 __init__() Method에서 변수초기화를 해주어야한다.
    # self는 객체 자기 자신을 의미한다. 호출할 때 Python에서 자동으로 해당 매개변수를 채워 넘겨준다.
    def __init__(self):
        self.color = 0xFF0000
        self.wheelSize = 19
        self.displacement = 3000
    
    def forward(self):
        print "전진"
    
    def backward(self):
        print "후진"
    
    def turn_left(self):
        print "좌회전"
    
    def turn_right(self):
        print "우회전"

# Car Class는 자료형이다. 즉, 아직 객체(Instance)가 되지는 않은 상태이다.
# Instance는 Class를 바탕으로 실체화된 것
# num = 123 [자료형: int, 변수: num]
# my_car = Car() [자료형: Car Class, 객체: my_car]
# my_car에 속한 멤버에 접근하려면 .을 이용해야 한다. (.은 ~의로 해석)
my_car = Car()
# my_car의 Wheel Size
print "차량의 바퀴 사이즈는 {0}inch 입니다.".format(my_car.wheelSize)
my_car.forward()
my_car.backward()
my_car.turn_left()
my_car.turn_right()