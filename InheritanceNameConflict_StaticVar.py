class Base:
    x = 10  # Base class static variable
    y = 15  # Base class static variable

    def __init__(self):
        x = 13  # local variable
        Base.x = 11  # updates Base class static variable

    def showBase(self):
        print("Base x =", self.x)


class Derived(Base):
    x = 20  # child class static variable

    def __init__(self):
        super().__init__()  # Creates Base class static variable
        Derived.x = 21  # Updates child class static variable

    def showDerived(self):
        print("Derived x =", self.x)

    @staticmethod
    def show():
        print(" Base.x =", id(Base.x), "\n", "Derived.x =", id(Derived.x))


print("Static variables are Class specific. So, they can be accessed directly using class object")
print("Before constructor call Base.x =", Base.x)
print("Before constructor call Derived.x =", Derived.x)
obj = Derived()  # constructor called implicitly
print("After constructor call Base.x =", Base.x)
print("After constructor call Derived.x =", Derived.x)
print(obj.x)    # object's class is preferred always or lets say variable hiding occurs
print(obj.y)    # object's class is preferred always or lets say variable hiding occurs
obj.show()
