# exception raised by user and handled by user defined mechanism using user defined exception class
class insuffiecietBalance(ZeroDivisionError):
    # newly created exception class must be a child class of any
    # predefined exception class otherwise it will not be treated as exception class
    def __init__(self, arg):  # function definition
        self.msg = arg


balance = 5000
wd = int(input("Enter Withdrawal Amount"))
try:
    if wd > balance:
        raise insuffiecietBalance("Not Enough Balance")
    balance = balance - wd
except insuffiecietBalance as i:
    print("Exception:", i.msg)
else:
    print("Withdrawal Amount", wd, "successfully")
finally:
    print("Current Balance is", balance)