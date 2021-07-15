a = lambda a, b: a + b
print(a(3, 44254))
# another way
b = (lambda a, b: a + b)(100, 200)
print(b)
print((lambda a, b: a if a > b else b)(10, 20))
# to get input from user pass input() as argument
print("Enter Two Numbers")
print((lambda a, b: a if a > b else b)(int(input()), int(input())))
# recursion in lambda
s = lambda a: 1 if a == 0 else a * s(a - 1)
print(s(5))