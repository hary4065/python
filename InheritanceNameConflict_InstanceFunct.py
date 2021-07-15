class Base:
    def __init__(self):
        self.a = 10  # instance variable

    def f1(self):   # instance function
        print("This instance function must have been called indirectly.")

    def f2(self):  # instance function
        print("Base F2()")

    @staticmethod  # declares following function as static
    def f3(x):  # Static function
        print("Static Function f3() defined in Base Class is called")


class Derived(Base):
    def __init__(self):
        super().__init__()
        self.a = 20

    def f1(self):
        print("Function Overriding occurs")

    def f2(self, x):
        print("Function Hiding may occurs")

    def CallBasef1(self):
        super().f1()

    @staticmethod  # declares following function as static
    def f3():  # static function
        print("Static function f3() defined in Derived Class Calls static function f3() defined in Base Class")
        try:
            super().f3()    # passes object implicitly
        except:
            print("Called function is static function. And super() method always passes object reference as argument to the function. But object reference as argument doesn't not exist here. So, an error is produced.")
        Base.f3(50)  # using class object we can call its own static function


obj = Derived()
obj.f1()  # Calling f1() defined in Derived Class but we cannot f1() defined Base Class
obj.CallBasef1()  # Indirect way to call f1() defined in Base Class
print("=========================================================")
try:
    obj.f2()  # Want to call f2() defined in base class by passing object itself implicity but failed
except:
    print('Function Hiding Occurs, giving "f2() missing 1 required positional argument" error')
obj.f2(100)  # calls f2() defined in Derived class
print("---------------------------------------------------------")
print("\nStatic function can be called using both class object and object of class.\n")
try:
    # Want to call static function defined in base class by passing one expected argument.
    obj.f3(50)
except:
    print("Function Hiding takes place. But Indirect access is possible via object")
# following statement calls static function f3() defined in Derived class. But object
# cannot differentiate between static and instance function. So, object itself
# is also passed like always, assuming instance function call.
# But interpreter knows that function is declared as static. And static function
# do not take object itself as argument. So, passed object referencec is discarded or ignored.
obj.f3()
print("=========================================================")
Derived.f3()  # calls static function f3() defined in Derived class
print("---------------------------------------------------------")
Base.f3(50)
