# TASK-2
# Program containing 7 different methods of list.

# initialisation of list
myList = [10,20,30,40,50]

# printing the list
print("My List= ", myList)

# printing the index of list element
myList.index(20)
print("Index of element 20 is = ", myList.index(20))

# changing the element on particular index
myList[3]=35
print("updated list is = ", myList)

# adding the element at the end of the list
myList.append(90)
print("list after adding element at the end is = ", myList)

# replacing elements of the list. [start:end]
myList[0:2]=[1,2]
print("list after replcing first two elements is = ", myList)

# removing elements from the list
myList[1:3]=[]
print("list after removing the elements is = ", myList)

# inserting element using index
myList.insert(3,89)
print("list after inserting the element = ", myList)

# removing element using index
myList.pop(1)
print("list after removing second element = ", myList)

# sorting the list
myList.sort()
print("sorted list = ", myList)

# printing maximum element
max(myList)
print("maximum element of the list is = ", max(myList))

# printing minimum element of the list
min(myList)
print("minimum element of the list is = ", min(myList))







