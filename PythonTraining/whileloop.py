num=int(input("Enter Input Number : "))
i=0
while(num > 0) :
    i = i+1
    print("Iteration ", i)

    # skip if i=6
    if (i == 6):
        print("skipping iteration ", i)
        continue

    if (i == 9):
        print("break out of loop ", i)
        break

    if (num > 0):
        print("the number is possitive", num)
    elif (num%2 == 0):
        print("the number is even", num)
    elif (num%2 != 0):
        print("the number is odd", num)
    if (num < 0):
        print("the number is negative", num)

    num = int(input("Enter Next Input Number : "))
else:
    print("I am here if all of the loop ran regularly meeting the condition of the regular loop condition ")

print('Bye - end of the while loop')
