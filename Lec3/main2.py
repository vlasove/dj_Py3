class A:
    a = 1 
    color = "blue"
    C = 10

class B(A):
    size = 23
    C = 20 


b = B()
print(b.C)