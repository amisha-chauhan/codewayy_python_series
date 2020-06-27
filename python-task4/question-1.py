#TASK-4
#QUESTION-1
#PROGRAM TO PRINT ALL THE PRIME NUMBERS

#NUMBER OF ROWS AND COLUMNS

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

# Initialize matrix
primeMatrix = []
primeMatrix = [[int(input()) for x in range (column)] for y in range(row)]

for i in range(row):
    for j in range(column):
        print(primeMatrix[i][j], end = " ")
    print()

#defining function to print prime numbers
def primeNumber(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
                return 0
        else:
            return 1

    else:
         return 0

print("matrix with all the prime numbers: ")
for i in range(row):
    for j in range(column):
        if(primeNumber(primeMatrix[i][j])):
            print(primeMatrix[i][j])
