#TASK-2
#Programme with 7 methods of dictionary

# initialising dictionary
dict = {'Name': 'Amisha', 'Age': 20, 'College': 'Amity University'}
print(dict)

# adding new key
dict['Course'] = "B.Tech CSE"
print (dict)

# printing element using keys
print("Name = ", dict['Name'])

# printing (keys,value) pair of dictionary items
dict.items()
print("key, value pairs of dictionary = ",dict.items())

# removing entry using key
del dict['College']
print(dict)

# length of dictionary
print("length of dictionary is = ",len(dict))

# sorting dictionary
print("sorted dictionary = ", sorted(dict))

# removing element from dictionary
print("latest dictionary = ", dict.popitem())




