"""
Коллекции
* set 
* str 
* list 
* tuple
* dict 
"""

# set() множество

a_set = set([1,1,1,1,1,20, 30, 40, "a", "b", "c"])
print(a_set)
print("Length:", len(a_set))
print("a" in a_set )
a_set.add(1020)


first_set = set([10, 20, 30])
second_set = first_set.copy()
second_set.add(100)

print("First:", first_set)
print("Second:", second_set)