# class of person

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
name = input('Enter your name: ')
age = input('Enter your age: ')

#  constructing a new object called person1
person1 = Person(name, age)
print(person1.name)
print(person1.age)