d = {}  # empty dictionary
d = dict()  # empty dictionary using dictionary constructor
p = {100: 'rahul', 101: 'ajay', 102: 1025}  # three element dictionary
q = {'one': 'rahul', 'two': 'ajay', 'thre': 105}  # string is written in quotes
# Dictionary constructor method takes only string as key, can't be a exp or number
d = dict(one='rahul', two='ajay', three=105)
print(p[100], q['two'], d['three'])  # error if invalid key
d['four'] = 'vijay'  # adds a value in the dictionary
d['one'] = 'Rahul'  # updates value in the Dictionary
d = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
for k in d:
    print("key=", k, "value=", d[k])
