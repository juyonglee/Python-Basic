# -*- coding: utf-8 -*-

animalList = ["Cat", "Dog"]
print "<Original animalList>"
print animalList

# append() - 리스트 끝에 새 요소를 추가한다.
print "\n<append() Example>"
print "Before animalList: {0}".format(animalList)
animalList.append("Tiger")
print "After animalList: {0}".format(animalList)

# extend() - 리스트를 이어 붙인다. (+ 연산자와 같은 기능을 수행한다.)
print "\n<extend() Example>"
print "Before animalList: {0}".format(animalList)
additionalAnimal = ["Lion", "Elephant", "Monkey"]
animalList.extend(additionalAnimal)
# animalList += additionalAnimal와 동일하다!
print "After animalList: {0}".format(animalList)

# insert() - 명시한 리스트 내의 위치에 새 요소를 삽입한다.
print "\n<insert() Example>"
print "Before animalList: {0}".format(animalList)
animalList.insert(0, "Panda");
print "After animalList: {0}".format(animalList)

# remove() - 매개변수로 입력한 데이터를 리스트에서 찾아서 발견한 첫 번째 요소를 제거한다.
print "\n<remove() Example>"
animalList.append("Monkey")
print "Before animalList: {0}".format(animalList)
animalList.remove("Monkey")
print "After animalList: {0}".format(animalList)

# pop() - 리스트의 마지막 요소를 리스트에서 제거한다.
print "\n<pop() Example>"
print "Before animalList: {0}".format(animalList)
animalList.pop()
print "After animalList: {0}".format(animalList)

# index() - But, 찾고자하는 데이터와 일치하는 요소가 없으면 오류가 발생!!
print "\n<index() Example>"
print "Index of Dog is {0}.".format(animalList.index("Dog"))

# count() - 매개변수로 입력한 데이터와 일치하는 요소가 몇 개 있는지를 반환한다.
print "\n<count() Example>"
animalList.append("Panda")
print animalList
print "Panda Count in animalList: {0}".format(animalList.count("Panda"))

# sort() - 리스트 내의 요소를 정렬합니다. 매개변수로 reverse = True를 입력하면 내림차순, 아니면 오름차순으로 정렬
print "\n<sort() Example>"
sortList = [1, 3, 10, 2, 5, 8]
print "Before sortList: {0}".format(sortList)
sortList.sort(reverse=True)
print "After sortList(내림차순): {0}".format(sortList)
sortList.sort()
print "After sortList(오름차순): {0}".format(sortList)

# reverse - 리스트 내 요소의 순서를 반대로 뒤집는다.
print "\n<reverse() Example>"
print "Before animalList: {0}".format(animalList)
animalList.reverse()
print "After animalList: {0}".format(animalList)