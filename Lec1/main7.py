d = {}
d["one"] = 20
d["two"] = None

d2 = d 
d2["one"] = 1000000000

# for k, v in d.items():
#     print(k, v)

print("d dict():", d)
print("d2 dict():", d2)