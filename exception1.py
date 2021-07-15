#exception raised by user, handled by user defined meachanism using predefined exception class
x = int(input("Enter Dividend"))
y = int(input("Enter divisor"))
try:
    if y == 0:
        raise ZeroDivisionError()
# custom message is supplied in exception handling block
    z = x / y
    print("Result is", z)
except ZeroDivisionError:
    print("Denominator can not be zero")
