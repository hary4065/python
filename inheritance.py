class person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def showName(self):
        print("Name :", self.name)

    def showAge(self):
        print("Age :", self.age)


class student(person):
    def __init__(self, r, n, a):
        self.rollno = r
        person.__init__(self, n, a)  # calls parent class constructor
        # Another way to call parent class constructor. object is passed implicitly
        super().__init__(n, a)

    def showRollno(self):
        print("Roll no :", self.rollno)


# child class constructor does not call parent class constructor unlike C++/Java Language
s1 = student(10, "Amit", 15)  # value goes to variable "r" in init()
print(s1.__dict__)
s1.showRollno()  # interpretr looks for function in object's class by function name. if not found then looks in parent class
s1.showName()
s1.showAge()
