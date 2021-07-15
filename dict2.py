words = {}
li = ['a', 'b', 'c', 'd', 'e']
for k in li:
    print("Enter word for letter", k)
    words[k] = input()
print(words)
d1 = words.copy()  # shallow copy is created
print(d1 is words,d1)
del (words['c'])    # deletes key 'c' and value associated to it
print(words)
words.clear()   # deletes all key-value pairs
print(words)