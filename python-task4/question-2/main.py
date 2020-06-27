#TASK-4
#QUESTION-2
#MODULE

import list
import strings
import operators

#calling function of lists
#square
x = int(input("enter the number of which square is to be calculated: "))

list.func_square(x)

#list
myList = [1, 4, 6, 9, 10]

#maximum and minimum
list.func_minMax(myList)
print()

#sum of elements
list.func_sum(myList)


#calling function of string
myString = input("enter the string")

strings.func_midChar(myString)
strings.func_vowel(myString)
strings.func_letter(myString)


#calling functions of operators
x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
z = int(input("enter the third number: "))
operators.func_and(x,y,z)
operators.func_or(x,y,z)
operators.func_not(x, y)
print()
