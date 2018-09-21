# num=int(input("Enter Input Number: "))
# if (num <0) :
#     print("Input is negative Number")
#
# num=int(input("Enter Input Number: "))
# if (num >0) :
#     print("Input is possitive Number")
#     print("Number", num, "sqrt is ", num*num)

# nested If statement
# can go down this way any number of levels
num=int(input("Enter Input Number: "))
if (num > 0):
    print("the number is possitive", num)
elif (num < 0):
    print("the number is negative", num)
else :
    print("the number is 0", num)

if (num > 0):
    print("the number is possitive", num)
elif (num%2 == 0):
    print("the number is even", num)
elif (num%2 != 0):
    print("the number is odd", num)
if (num < 0):
    print("the number is negative", num)


print('Bye')
