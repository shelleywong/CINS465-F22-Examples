# Python 3 example/reference code
# CINS465 Fall 2022
# Shelley Wong

print("Hello World!")

# Example of Python: dynamic strongly type language
x = 42
print(type(x))
print("hello " + str(x)) # strongly typed
x = 3.14  # dynamic typing
print(x)
print(type(x))

# create and use a list
mylist = [42, 3.14, "hello world"]
print(mylist)
# concatenate and prepend
mylist += ["CINS465"]
mylist = [0.0] + mylist
print(mylist)
# access list elements
print("List element index 2: " + str(mylist[2]))
print("List element index 4: " + mylist[4])
# for loop example
print()
for elem in mylist:
    print(elem)
print()
# dictionary Example
mydi = {'a': 113, 'b': 42}
print(mydi)
mydi['b'] = 24
mydi['c'] = 9.9
mydi['d'] = "hello"
print(mydi)
print()

# class example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " " + str(self.age)

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

p1 = Person("Ada", 31)
print(p1)
p1.setAge(32)
print(p1.getAge())

# Python inheritance Example
class Student(Person):
    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.grade = grade

p2 = Student("Alan", 42, 12)
print(p2)
