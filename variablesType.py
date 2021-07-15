class Account:
    roi0 = 3.5  # static variable

    def __init__(self, a):  # creates instance variable "accn" when object is created
        self.accn = a  # instance variable
        Account.roi1 = 4.5  # static variable

    def f1(self, a, b):  # function taking atleast one argument are called instance member function
        accn = a  # without object reference local variable to function is created instead of creating/updating  instance variable "accn"
        self.accn = a
        self.balance = b
        Account.roi2 = 4.75  # static variable created using instance member function

    @staticmethod  # optional as function itself doesn't expect arguments
    def f2():  # Function not taking object as reference called static member function or static function
        x = 123  # local variable
        # self.x=123 is not valid as no object refernce exist in this function
        Account.fdroi = 5.20  # static variable

    @staticmethod  # required as function expect arguments but we want it to be static function
    def f3(m, n):
        print("Sum is", m+n)

    @classmethod  # expect to receive class object
    def f4(m, n):
        m.fdmin = 10000  # static variable is created
        Account.fdmin = 10000*1.2  # static variable is updated
        print("Minimum FD value is", n)


acc1 = Account(1012)  # instance variable "accn" is created
# prints list of all instance variable if exist otherwise print empty dictionary.
print(acc1.__dict__)
acc1.f1(1012, 6000)  # instance variable "balance" is created
print(acc1.__dict__)  # To print list of all instance variable
acc1.Lastwdrl = 1000  # instance variable "Lastwdrl" is created
acc1.balance -= acc1.Lastwdrl  # instance variable Lastwdrl is updated
print(acc1.__dict__)  # To print list of all instance variable
# In following, Function expect object of class as referrence. So, cannot be called using class object
#Account.f1(1012, 7000)
# function do not expect object as reference. so values goes to respected variables
Account.f3(4, 7)
# in following function doesn't expect object as reference. but two argument values are expected
# acc1.f3(4)
acc1.roi = 3.75  # static variable is updated
Account.f4(123456789)
Account.grade = 9250  # static variable is created
print("grade pay is", acc1.grade)
print(acc1.__dict__)    # prints list of instance variable if object is used
# prints list of static variables if class object is used
print(Account.__dict__)
