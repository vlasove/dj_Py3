"""
Управляющие конструкции:
* if 
* while/for
* def / lambda
"""
# Условный оператор
if not []:
    a = 2
    b = 3 
    c = 20
    print(a,b,c)
else:
    print(a,b,c)


if expression:
    body 
elif expression1:
    body1
.... 
else:
    body_else



# Циклы
while True:
    password = input("Enter password:")
    if len(password) < 10 and password.isalnum():
        print("Weak password, try again")
        continue
    else:
        break 


for  i in range(100, 1, -2):
    print("i", i, "i**2", i**2)

n = int(input()) 
for _ in range(n):
    name = input()
    ....