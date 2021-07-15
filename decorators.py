# decorator definition
def decor_result(result_function):
    def distinction(marks):
        for m in marks:
            if m > 75:
                print("Congrats, You have got distinction")
        else:
            result_function(marks)

    return distinction  # Invoking function


# funtion definition
@decor_result  # says for call to folloeing function call decorator.
def result(marks):
    for m in marks:
        if m > 33:
            pass
        else:
            print("FAIL")
            break
    else:
        print("Pass")


result([48, 54, 89, 41, 34, 65, 88])
# result() as input to decorator. ouput distinction() is produced