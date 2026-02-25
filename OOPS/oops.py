class Person:
    name = "Harry"
    occupation = "Engineer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "Abhi"
a.occupation = "Doctor"
a.info()

b = Person()
b.info()