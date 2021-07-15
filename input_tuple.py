t = tuple(input("Enter a tuple"))
# takes every character as tuple elements thus not useful
print(t)
t = eval(input("Enter a tuple"))
# using eval() we can also get a list from user
# to get list from user, user must enter value in square brackets
print(t)
t = 1, 2, 3, 4, 5, 6, 1
print(t.count(1))  # returns number of occurence of an element in tuple
print(t.index(1))  # returns index of the element in tuple
print(min(t))  # returns min value from tuple
print(max(t))  # returns max value from tuple
