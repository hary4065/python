t = ()  # empty tuple
p = (10)  # variable is declared
t = (10,)  # tuple is created
t = 10, 20, 30  # Declares a tuple
l = [1, 2, 3, 4]
t = tuple(l)
# t = tuple(10, 20, 30)  doesn't declares a tuple
t = tuple((10, 20, 30))  # declares a tuple
t = (10, "abc", 's', 10.56)
# print(t[4])  index out of range error
for x in t:
    print(x)
i = 0
while i < len(t):
    print(t[i])
    i += 1
t = t+(1, 2, 3, 4)  # new tuple is created and stored
print(t[0::])  # tuple elements acces using slicing operator
