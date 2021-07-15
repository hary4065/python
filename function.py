def info(**k):
    print("Person Information")
    for key, value in k.items():
        print(key, "-", value)


info(name="sameer", age=87)
info(name="Rahul", marks=457)
info(name="Vijay", empid=1527, salary=35000)
