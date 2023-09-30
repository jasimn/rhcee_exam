
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # def __str__(self):
        # return f"person name is {self.name} and age is {self.age}"
    def __repr__(self):
        return f"person {self.name},age {self.age}"
        
realm=Person("rahul",34)

print(realm)