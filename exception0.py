# exception raised by user but but handled by default exception handling mechanism
x = int(input("Enter Dividend"))
y = int(input("Enter Divisor"))
if y == 0:
    raise ZeroDivisionError("Divisor can't be zero")
# custom message is passed in exception constructor if
# exception is to be handled by default exception mechanism
z = x / y
print("Result is", z)
