s = {10, 20, 10, 30}
print(s)
s = {}  # doesn't create an empty set but it is dictionary
t = set()  # creates an empty set
t = set(10)  function is supposed to take a sequence not a value
t = set(10, 20, 30) single value which must be a sequence
t = set([10, 20, 30])  # set is created
t.add(40.12)  # heterogenous data can be stored in set
t.add(30)  # Duplicate value is discarded
t.add((35, 40))  # Duplicate value is discarded
print(t)
# update function performs union of all sequences passed as argument.
t.update({1, 2, 3}, (2, 3, 6))  # can take multiple sequence as argument.
print(t)
t.discard(9)  # removes item from set. no error if item is not in set
t.remove(8)  # removes item from set if exist otherwise produces an error
t.add([1, 2])  # List cannot be an element of set
print(t)
p = {1, 2, 3, 4}
t = t.intersection(p)  # returns intersection of sets
print(t)
print(t.issubset({1, 2, 3, 4}))
print(t.issuperset({1, 2}))
print(t.pop())  # remove a random item from non empty set.
t.copy()    # returns a copy of the set
t = set("ABCDEFGHIJKLMNOP")  # Doesn't preserve the sequence
print(t)
