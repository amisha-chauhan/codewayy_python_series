#TASK-4
#QUESTION-2-A

#function to calculate square of a number
def func_square():
    x = int(input("Enter the number for which square is to be calculated: "))
    square = x * x
    print("the square of the number is: ",square)
func_square()


#creating a list
myList = []
list = int(input("length of list: "))
for num in range(list):
    numbers = int(input())
    myList.append(numbers)
print("the list is: ",myList)

#function to find minimum and maximum element from the list
def func_minMax():
    minimum = myList[0]
    for i in myList:
        if(minimum > i):
            minimum = i
    print("the minimum element is: ", minimum)


    maximum = myList[0]
    for i in myList:
        if(maximum < i):
            maximum = i
    print("the maximum element is: ", maximum)
func_minMax()

#function to find sum of elements of the list
def func_sum():
    sum = 0
    for n in range(0, list):
        sum = sum + myList[n]
    print("sum of element is: ", sum)
func_sum()
