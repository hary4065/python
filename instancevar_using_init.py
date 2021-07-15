class test:
    i = 10

    def __init__(self, a, b):
        self.a = a  # instance variable a is created and passed value is assigned
        self.b = b  # instance variable b is created and passed value is assigned
        print("init function is used to create instance variable")

    def f1():
        print("cannot access instance variabele")

    def f2(self):  # self points to object
        self.a = "Instance varaible access using instance method"
        print(self.a)

    def f3(x, y, z):
        x.a = y  # x points to object
        x.b = z
        print(x.a, x.b)


# object itself is passed as first argument to init function
# values 3 and 4 are passed to instance variable of object
t1 = test(3, 4)
t2 = test(10, 20)
print(t1.a, t1.b)  # instance variable access
print(t2.a, t2.b)
# function doesn't expect any argument but still object itself is passed
t1.f1()  # produce same effect as writing f1(t1) statement but we want it to be called as f1()
t1.f2()  # Same as f2(t1), object itself is passed implicitly
t1.f3(10, 20)  # instance variabele access
