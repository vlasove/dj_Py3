"""
Классы, ООП, наследование
"""

"""
Инкапсуляция - способность объектов сркывать критически важные свойства от пользователя. (Пример: радио приемник)

Полиморфизм - способность объекта проявлять свои свойства по-разному в зависимости от окружающей ситуации (1 + 1, '1' + '1')

Наследование - способность объекта использовать уже созданные инструкции (другие классы) при создании самого себя.
"""

class Book:
    def __init__(self, title:str, author:str):
        self.__title = title 
        self.__author = author 

    def __stable(self):
        pass 

    def __str__(self):
        return "Book<Title: {} , Author: {}>".format(self.__title, self.__author)

    def __del__(self):
        print("This object with GB: {} {}".format(self.__title, self.__author))


b = Book("a", "b")
print(b)
b._Book__stable()



class Circle:
    def __init__(self, R:int=0):
        self.__r = R 

    def area(self):
        return 3.14 * self.__r **2

class Rectangle:
    def __init__(self, A:int=0, B:int = 0):
        self.__a = A 
        self.__b = B 

    def area(self):
        return (self.__a *self.__b)

    



c1 = Circle(1)
c2 = Circle(20)
c3 = Circle(25)

r1 = Rectangle(10, 20)
r2 = Rectangle(30 ,40)

figures = [c1, c2, c3, r1, r2]
total_area = 0
for figure in figures:
    total_area += figure.area()

