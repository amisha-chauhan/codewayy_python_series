#TASK-4
#QUESTION-2-A

#function to calculate square of a number
def func_square(x):
    square = x * x
    print("the square of the number is: ",square)




#function to find minimum and maximum element from the list

#minimum
def func_minMax(myList):
    minimum = myList[0]
    for i in myList:
        if(minimum > i):
            minimum = i


#maximum
    maximum = 0
    for i in myList:
        if(maximum < i):
            maximum = i
    print("the maximum element is: ", maximum)


#function to find sum of elements of the list
def func_sum(myList):
    sum = 0
    for i in myList:
        sum = sum + i
    print("sum of element is: ", sum)
