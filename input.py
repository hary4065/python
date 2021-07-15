x = input()  # return string
# return type is converted wrt to input type. like if integer is entered, return type will be an int.
x = eval(input())
# reading multiple inputs from user
x, y = input(), input()
x, y = input().split()   # by default input is splited on basis of space character
# Input is splited on basis of comma character, a list of string is returned
x, y = input().split(',')
# list is returned then each element is converted to int. then it is assigned to var
a, b, c = [int(x) for x in input("Enter Date").split('/')]
# input is needed to be stored as input type
a, b, c = [eval(x) for x in input().split(',')]
# we want sequence as input
li = tuple([eval(x) for x in input("Enter three values").split(',')])
li = set([eval(x) for x in input("Enter three values").split(',')])
# range limits the number of input in dictionary
li = dict(input().split('-') for k in range(3))
# another method to input values in dictionary
li = {x: input() for x in range(1, 5)}
li = {input("Key"): input("Value") for x in range(3)}
# want key as integer
li = {int(input("Key")): input("Value") for x in range(3)}
