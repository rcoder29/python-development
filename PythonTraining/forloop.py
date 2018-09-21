#for i in (0,1,2,3,4,5,6,7,8,9,10):
for i in range(0,12,3):

    # skip if i=6
    if (i == 6):
        print("skipping iteration ", i)
        continue

    if (i == 9):
        print("break out of loop ", i)
        break

    print("Iteration ",i)
    num=int(input("Enter Input Number : "))
    if (num > 0):
        print("the number is possitive", num)
    elif (num%2 == 0):
        print("the number is even", num)
    elif (num%2 != 0):
        print("the number is odd", num)
    if (num < 0):
        print("the number is negative", num)
else:
    print("I am here if all of the loop ran regularly, without any break ")

print('Bye - end of the for loop')
