# class Person:
#     def __init__(self,name, occ):
#         self.name = name
#         self.occupation = occ

#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a = Person()
# a.name = "Abhi"
# a.occupation = "Doctor"
# a.info()

# b = Person()
# b.info()

# a = Person("Harry", "Enginner")
# a.info()

# b = Person("Diksha", "HR")
# b.info()

# def greet(fx):
#     def mfx(*args):
#         print("Hello")
#         fx(*args)
#         print("Bye")
#     return mfx

# @greet
# def add(a,b):
#     print(a+b)

# add(2,3)
# greet(add)(1,2) #This also gives same output, need to remove @greet 

# class Myclass:
#     def __init__(self, value):
#         self._value = value

#     @property
#     def myValue(self):
#         return self._value    
    
#     @myValue.setter
#     def myValue(self, value):
#         self._value = value

#     def show(self):
#         print(f"Value is {self._value}")   

# a = Myclass(10)         
# print(a.myValue)
# a.myValue = 50
# print(a.myValue)

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def printName(self):
#         print(self.name)

#     def printId(self):
#         print(self.id)

# class Person(Employee):
#     def show(self):
#         print("Im a Human")

# a = Employee("Harry", 18)
# a.printName()
# a.printId()

# b = Person("Divya", 38)
# b.printId()
# b.printName()
# b.show()

# class Myclass:
#     def __init__(self, name, id):
#         self._Name = name 
#         self.__id = id

# obj = Myclass("Harry", 10)
# print(obj._Name)
# # print(obj.__id)#Gives Error 
# print(obj._Myclass__id)#Accessing indirectlyy (name mangling)

# class Library :
#     def __init__(self, n , l):
#         self.no_Of_books = n
#         self.books = l

#     def addbook(self, item):
#         self.books.append(item)
#         self.no_Of_books = len(self.books)

#     def printbook(self):
#         print(f"The {n} Books are")
#         for item in self.books:
#             print(item)

#     def getbookCount(self):
#         return len(self.books)

#     def checkLibrary(self):
#         if self.no_Of_books == len(self.books):
#             print("Good Management")
#         else :
#             print("Something is wrong in this")     


# n = 2
# l = ["book1", "book2"]
# a = Library(n, l)
# a.printbook()
# a.addbook("Book3")
# a.printbook()
# print(a.getbookCount())
# a.checkLibrary()

# class Example :
#     def __init__(self):
#         pass

#     @staticmethod
#     def Add(a,b):
#         print(f"Sum of {a} and {b} is {a + b}")    

# obj = Example()
# obj.Add(2,3)
# Example.Add(5,5)         

# class Company:
#     CompanyName = "XYZ"
#     def __init__(self, name):
#         self.name = name

#     def printDetais(self):
#         print(f"{self.name} Works at {self.CompanyName}")    


# obj = Company("Harry")
# obj.printDetais()

# obj1 = Company("Axar")
# obj1.CompanyName = "ABC"
# obj1.printDetais()

# import os
# class ClearCluster:
#     def __init__(self):
#         pass
    
#     def renameFiles(self, folderPath, ext):
#         files_found = os.listdir(folderPath)

#         for i, item in enumerate(files_found):
#             if item.endswith(".png"):
#                 print(f"Item = {item} and i = {i}")
#                 os.rename(f"{folderPath}/{item}", f"{folderPath}{i}.png")

# obj = ClearCluster()
# obj.renameFiles("DATA", ".png")


# class Example :
#     companyName = "ABC"

#     def __init__(self):
#         pass

#     @classmethod
#     def changeName(cls,name):
#         cls.companyName = name   

#     def showName(self):
#         print("Company Name :", self.companyName)    

# e = Example()
# e.showName()
# e.changeName("XYZ")
# e.showName()
# print(Example.companyName)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"{self.name} and {self.age}")

#     @classmethod
#     def fromStr(cls, string):
#         return cls(string.split("-")[0], string.split("-")[1])

# p = Person("Harry",30 )  
# p1 = Person.fromStr("john-26")

# x = [1,2,3]
# print(dir(x))

# class Example:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p = Example("Harry",24)
# print(p.__dir__)        

# print(help(str))

# class Example:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show():
#         print("This is Parent class")    

# class child(Example):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def show():
#         print("The child Method")
#         super().show()

# p = child("Harry",24)
# print(p.name)
# print(p.age)

# class Exmaple:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"The Name is {self.name} str"

#     def __repr__(self):
#             return f"The Name is {self.name} repr"
    
#     def __call__(self, *args, **kwds):
#          print("Im the Call method")

# ex = Exmaple("Haryy")
# print(str(ex))
# print(repr(ex))
# ex()         

# class shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def area(self):    
#         return self.x * self.y
    
# class circle(shape):
#     def __init__(self, x, y):
#         super().__init__(x, y)

#     def area(self):
#         return 3.14 * super().area()        

# rec = shape(3,4)
# print(rec.area())

# c = circle(3,4)
# print(c.area())

# class Vector:
#     def __init__(self, i, j , k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __add__(self, other):
#         return Vector(self.i + other.i , self.j + other.j , self.k + self.k)    
    
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
    
# V1 = Vector(3,4,5)
# print(str(V1))

# V2 = Vector(4,5,6)
# print(str(V2))

# print( V1 + V2)

# class Person :
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"The Name is  {self.name}")    

# class Dancer :
#     def __init__(self, dance):
#         self.dance = dance

#     def show(self):
#         print(f"The Dance is  {self.dance}") 

# class Example(Person, Dancer):
#     def __init__(self, name, dance):
#         self.name = name
#         self.dance = dance

# ex = Example("Shreya", "Katak")
# print(ex.name)
# print(ex.dance)
# ex.show()

# print(Example.mro())
        

#Merge pdf Exercise 
# from PyPDF2 import PdfWriter
# import os

# merger = PdfWriter()
# files = [files for file in os.listdir() if file.endswith(".pdf")]

# for pdf in files:
#     merger.append(pdf)

# merger.write("Merged.pdf")
# merger.close()    