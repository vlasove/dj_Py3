"""
Множественное наследование
"""

class A:
    def __init__(self, name:str):
        self.name = name
        print("Construct for A class working") 

class B:
    FIELD = "B"
    def __init__(self, lastname:str):
        self.lastname = lastname
        print("Construct for B class working") 

class E:
    FIELD = "E"


class C(A,B, E):
    def __init__(self, name, lastname, age:int):
        self.age = age 
        #super().__init__()
        A.__init__(self, name)
        B.__init__(self, lastname)

c = C("Bob", "Dylan", 23)
print(c.age, c.name, c.lastname, c.FIELD)