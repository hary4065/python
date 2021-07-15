class Base:
    def __init__(self):
        self.a = 10

    def showBase(self):
        print("Base a =", self.a)


class Derived(Base):
    def __init__(self):
        self.a = 20
        # if this statement is executed in last then derived class creates instance variable. But if executed first then parent class creates instance variable.
        super().__init__()

    def showDerived(self):
        print("Derived a =", self.a)


obj = Derived()  # Child constructor creates variable "a=20"
obj.showDerived()  # variable "a" is common to both class
obj.showBase()
