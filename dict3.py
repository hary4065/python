li = [1, 2, 3, 4, 5]
d = {}
d2 = d.fromkeys(li, "ABC")
print(d2)
# to get value of key two method are
print(d2[2])  # error if invalid key
print(d2.get(6))  # prints 'None' if invalid key is passed
# pop function removes key-value pair from set and returns value
print(d2.pop(3))
print(d2)
t = d2.popitem()  # random key value pair is removed from set
print(type(t), t[0], t[1])  # removed key value pair is returned as tuple
print(d2)
