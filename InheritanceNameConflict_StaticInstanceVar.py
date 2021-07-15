class Base:
    x = 10

    def __init__(self):
        self.x = 20

    @staticmethod
    def f1():
        print("Static Member funtion")

    def f1(self):  # instance function
        print("Static function is invalidated as instance Funtion has same name. This is beacuse concept of function overloading not exist here")


class Derived(Base):
    x = 30

    def __init__(self):
        super().__init__()


obj = Derived()
# Instance variable is preferred over static variable
# static variable are class specific
print(obj.x, Derived.x, Base.x)
try:
    Base.f1()
except:
    print("Supposed to call static function, but calls instance function")
obj.f1()    # instance function call
# All of the functions having same name declared in a class are invalidated/ignored
# except the last one. It doesn't care whether instance function is ignored static function.
