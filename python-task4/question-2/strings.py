#TASK-4
#QUESTION-2-B

#FUNCTION FOR STRING

#INITIALISE STRING
def func_string():
    myString = input("enter the string: ")

#finding middle char
    if(len(myString) % 2 == 0):
        print("middle char of string is: ", myString[(int(len(myString) / 2) - 1)] + " " + myString[(int(len(myString) / 2))])
    else:
        print("middle char is: ", myString[(int(len(myString) / 2))])

              
#finding vowels
    vowel = 0
    for x in myString:
        if(x == 'a' or x == 'e' or x == 'i ' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
              vowel = vowel + 1
    print("vowels are: ", vowel)


#calculate number of letters
    count = 0
    for x in myString:
        count += 1
    print("number of letters in string are: ",count)
func_string()
    
              
