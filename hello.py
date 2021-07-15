w = "That's"  # We print single quote in output
x = '"MySirG".'    # we can print a double qouted string
y = """Teacher's Day is
"My Day"."""  # can print both single and double quoted data in multiline
z = '''Don't stop
"me today".'''  # can print both single and double quoted datat in multiline
print(w, x)
print(y)
print(z)
print(len(z))  # returns length of the string
print(z.index("stop"))  # return index of the string
print(z.count('"'))  # return count of the string
print(w[1])  # returns character at index
# negative index starts from -1 right to left
print(w[-3])  # returns character at index
li = range()
print(li[1], li[-2])
