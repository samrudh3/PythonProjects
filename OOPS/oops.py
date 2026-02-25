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

def greet(fx):
    def mfx(*args):
        print("Hello")
        fx(*args)
        print("Bye")
    return mfx

@greet
def add(a,b):
    print(a+b)

add(2,3)
# greet(add)(1,2) #This also gives same output, need to remove @greet 