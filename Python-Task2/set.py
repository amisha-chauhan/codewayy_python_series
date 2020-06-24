#TASK-2
#Programme containing 7 methods of sets.

#initialising the set
set_1 = {1,2,3,4,5,6,6,7,3,4,6}
set_2 = {1,6,9,10,12,14,16}

#printing the set
print (set_1)

# adding element to the set
set_1.add(12)
print("set after adding element = ", set_1)

# removing specific element from the set
set_1.discard(7)
print("updated set = ",set_1)

# intersection of two sets
set_3 = set_1.intersection(set_2)
print("intersection of two sets = ",set_3)

# difference in two sets
set_3 = set_1.difference(set_2)
print("difference of sets is = ", set_3)

# union of two sets
set_3 = set_1.union(set_2)
print("union of two sets = ", set_3)

#symmetric difference of two sets
set_3 = set_1.symmetric_difference(set_2)
print("symmetric difference if two sets is = ", set_3)

# removing duplicates from the list using sets
list_1 = [1,22,26,27,22,27,23,29]
list_2 = set(list_1)
list_2 = list(set(list_1))
print(list_2)




