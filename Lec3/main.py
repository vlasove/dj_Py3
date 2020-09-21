"""
Декораторы - функция, расширяющая статичные возможности
существующего кода.
Например, декоратор может выполнять проверку сушествования подключения,
существования бд и валидность TimeZone.  
"""
def my_decorator(func):
    def wrapper():
        print("Before func() in @decorator")
        func()
        print("After func() in @decorator")
    return wrapper

def my_decorator2(func):
    def wrapper():
        print("Before func() in @decorator2")
        func()
        print("After func() in @decorator2")
    return wrapper

@my_decorator2
@my_decorator
def hello():
    print("Hello!")

# hello = my_decorator(hello)

hello()
    