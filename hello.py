
#07-aug-2026
#list1 = [1,2,3,4,5]
#print(list1)
#print (list1[3])
#list1[4]=8
#print(list1[4])
#print(list1)
#traverse the list
#list2=[12,15,28,37]
#print(list2[::-1])
#count even_element and odd_element present
#even_count=0
#odd_count=0
#list1=[12,14,16,18,20,22]
#for i in range(0,len(list1)-1):
 #   if list1[i]%2==0:
  #   odd_count +=1
#print(even_count)
#print(odd_count)
#find the average of elemant prisent in list
# append()
"""l1 =[1,2,3,4,5,6,7,1]
print (l1)
l1.append(50)
print (l1)
l1.remove(7)
print(l1)"""

#  insert() remove() 
# pop() 
#l1 =[1,2,3,4,5,6,7,1]
#l1.pop(1)
#print (l1)
#insert 

#l1.insert(2 "25")
#print (l1)
# len()
# extend() reverse() sort() clear() copy()
# count()
#for i in list1:
#sum = sum+1
#average = sum/len(list1)
#print(average)


#tuple
"""t1 = (1,5,2,5,4,2)
print(t1)
print (type(t1))
t1.append (4)
print(t1)"""
#set
"""s1 = {1,5,2,5,4,2}
print(s1)
print (type(s1))
s1.remove(5)
print(s1)
s1.pop()
print(s1)
s1.add(12)                                          
print(s1)"""

#13/08/2026
#indentation
"""def display():
    print("Display Function")


display()


class Student:

    def display(self, name, city):
        print("Display from student")
        print(name)
        print(city)


s = Student()
s.display("Shivam", "Lucknow")"""
# Constructor

"""class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetail(self):
        print("Display from student")
        print(self.name)
        print(self.id)
        print("----------------")

s1 = Student("Shivam", 101)
s2 = Student("Rahul", 102)
s3 = Student("Aman", 103)
s4 = Student("Rohit", 104)
s5 = Student("Ankit", 105)

s1.showDetail()
s2.showDetail()
s3.showDetail()
s4.showDetail()
s5.showDetail()"""

# Inheritance

class Animal:
    def show(self):
        print("Animal show method")


class Cat(Animal):
    def makesound(self):
        print("Meowww")


c = Cat()
c.show()
c.makesound()

class dadaji:
    def show(self):
        print("show from Dadaji")


class papaji(dadaji):
    def output(self):
        print("output from Papaji class")


class betaji(papaji):
    def display(self):
        print("display from Betaji")


b = betaji()

b.show()
b.output()
b.display()