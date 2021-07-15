try:
    print("Line1")
    # 3 + '4'
    print("Line2")
    try:
        print("Nested Line1")
        # 5/0
        print("Nested Line2")
    except ZeroDivisionError:
        print("Nested Exception: Cannot Divide by zero")
    finally:
        print("Nested Finally")
    print("Line3")
except TypeError:
    print("Exception: Cannot add integer and string")
finally:
    print("Finally")
