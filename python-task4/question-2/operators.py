#TASK-4
#QUESTION-2-C

#FUNCTION FOR ALL LOGICAL OPERATORS
x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
z = int(input("enter the third number: "))

#And operator
def func_and(x,y,z):
    if x > y and y > z:
        print("first number is greatest")
    if x < y and y < z:
        print("first number is smallest")
func_and(x,y,z)

#or operator
def func_or(x,y,z):
    if x > y or x > z:
        print("x is greatest number")
    else:
        print("x is not the greatest")

    if y > x or y > z:
        print("y is the greatest number")
    else:
        print("y is not the greatest")

    if z > x or z > y:
        print(" z is the greatest number")
    else:
        print("z is not the greatest")
func_or(x,y,z)

#not operator
def func_not(x, y):
    if not x > y:
        print("y is greater")
func_not(x, y)

