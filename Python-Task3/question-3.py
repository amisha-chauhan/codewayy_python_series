#TASK-3
#QUESTION-3

#Printing all the numbers till 10 except 3 and 7

#USING FOR LOOP

#Method-1
list =[1,2,3,4,5,6,7,8,9,10]

for num in list:
    if(num == 3 or num == 7):
        continue
    else:
        print(num)

#Method-2
for i in range(1,11):
    if(i == 3 or i == 7):
        continue
    print(i)

#USING WHILE LOOP
    x = 1
while (x != 11):
    if (x == 3 or x == 7):
        x += 1
    else:
        print(x)
        x += 1




