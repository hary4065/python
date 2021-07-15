x = "HelloWorld"
print(x[::])    # slice from index 0 to string's end by 1 step
print(x[2:])  # slice from index 2 to string's end by 1 step
print(x[2::])  # slice from index 2 to string's end by 1 step
print(x[:2:])  # slice from index 0 to 2 by 1 step
print(x[:2])  # slice from index 0 to 2 by 1 step
print(x[::2])  # slice from index 0 to string's end by 2 step
print(x[3:6:])  # slice from index 3 to 6 by 1 step
print(x[4:7:2])  # slice from index 4 to 7 by 2 step
# slice from index -4 to 2 by 2 step moving from left to right.
print(x[-4:2:2])  # no output is produced.
print(x[-4:1:-2])  # slice from index -4 to 1 by -2 step.
print(x[len(x)::-1])  # string is reversed
print(x[::-1])  # string is reversed
print(x.lower())  # string in lowercase
print(x.upper())  # string in uppercase
print(x.startswith("H"))  # whether string starts from H
print(x.endswith("d"))  # whether string ends with H
# split the string wherever o is occurs. character is not included in splits
print(x.split('o'))
