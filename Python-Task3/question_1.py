#TASK-3

# 1) A program with 5 different functions

# a) Function that returns full name

def yourFullName(firstName, lastName):
    Name = firstName + ' ' + lastName
    print("Your name is: ", Name)

# b) Function that returns the total marks

def yourTotalMarks():
    Phy_Marks=float(input("Enter your physics marks: "))
    Maths_Marks=float(input("Enter you maths marks: "))
    Chem_Marks=float(input("Enter you chemistry marks: "))
    Eng_Marks=float(input("Enter you english marks: "))
    Cs_Marks=float(input("Enter you computer science marks: "))
    global grandTotal
    grandTotal = Phy_Marks + Maths_Marks + Chem_Marks + Eng_Marks + Cs_Marks
    print("The grand total of your marks is: ", grandTotal)

# c) Function that returns percentage

def yourPercentage(grandTotal):
    global percentage
    percentage = (grandTotal/5)
    print("Your percentage is: ", percentage)

# d) Function that returns grade

def yourGrade(percentage):
    if (percentage>=95):
        print('Your grade is A')
    elif (percentage>=85 and percentage<95):
        print('Your grade is B')
    elif (percentage>=75 and percentage<85):
        print('Your grade is C')
    elif (percentage>=65 and percentage<75):
        print('Your grade is D')
    else:
        print(" SORRY YOU FAILED! ")

# e) Function that returns all the previous functions

def allStudentDetails():
    yourFullName()
    yourTotalMarks()
    yourPercentage(grandTotal)
    yourGrade(percentage)

# To call this function
allStudentDetails()    
