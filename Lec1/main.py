"""
В языке 5 базовых типов:
* int
* float
* bool
* str
* None 
"""

a_int, b_float = 10, 20 
a_int += 20

print("Sum:", a_int + b_float)
print("Sub:", a_int - b_float)
print("Mult:", a_int * b_float)
print("Div:", a_int / b_float)

print("Int div:", a_int // b_float)
print("Reminder:", a_int % b_float)
print("Pow:", a_int ** b_float)

# Конструкция цепного присваивания
a = b = c = 3 
PRODUCTION_PORT = DEV_PORT = "localhost:8080"


# Логический тип
a_bool, b_bool = True , False 

print("and", a_bool and b_bool)
print("or", a_bool or b_bool)
print("not", not a_bool)


print("Res:", a_bool + b_bool ** a_bool)


# Строка str 
name_str = "Hello"
print("Length:", len(name_str))
print("e" in name_str)
print(name_str * 10)


# NoneType (Ничего)
a_none = None 
