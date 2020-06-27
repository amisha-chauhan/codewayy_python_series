#TASK-4
#QUESTION-2
#MODULE

import list
import strings
import operators

#calling function of lists
myList = (int(input("enter the elements of list: ")))
list.func_square(x)
list.func_minMax(myList)
list.func_sum(myList)
print()

#calling function of string
myString = input("enter the string")
strings.func_string()
print()

#calling functions of operators
x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
z = int(input("enter the third number: "))
operators.func_and(x,y,z)
operators.func_or(x,y,z)
operators.func_not(x, y)
print()
