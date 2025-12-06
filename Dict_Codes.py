#1. Create a dictionary and print all its keys.
d={
    'a':1,
    'b':2,
    'c':3
}
print(d)
print(d.keys())

#2. Create a dictionary and print all its values.
print(d.values())

#3. Create a dictionary and print all key–value pairs using a loop.
for i , j in d.items():
    print(i , j)

#4. Add a new key-value pair to an existing dictionary.
d.update({'d':4})
print(d)

