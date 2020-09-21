"""
Функция - обособленный кусок кода, к которому можно обращаться по необходимости 
"""
def my_func(a:int, b:int =10) -> int:
    """
    Test docstring
    """
    return a + b

lambda_func_res = (lambda a,b  : a + b)(10, 20)
print("Lambda::", lambda_func_res)






res = my_func(20, 30)
print(res)





