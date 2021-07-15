y = 10  # global variable


def f1(a):
    x = 5  # Variable "x" and "a" are local to function
    print("Inside Function Local variable x =", x, "and a =", a)
    print("Inside Function Global variable y =", globals()['y'])
    # In a function, local and global variable with same name cannot exist at
    # the same time. But one at a time is possible
    global y  # Tells interpreter that y is global variable.
    y = 20  # if variable y exist globally it is updated otherwise created
    print("Local variable is always preferred over global variable")
    print("In Function Global variable y =", y)


f1(30)
print("Outside function Global variable y =", y)
print("Variable x is local to function. So, it is not accessible")
