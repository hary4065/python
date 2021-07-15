class Base:
    x = 10

    def __init__(self):
        self.x = 20

    def f1(self):
        print("Static function is invalidated as instance Funtion has same name. This is beacuse concept of function overloading not exist here")

    @staticmethod
    def f1():
        print("Static Member funtion")


class Derived(Base):
    def __init__(self):
        self.b = 40


obj = Derived()
Base.f1()
Derived.f1()
obj.f1()
