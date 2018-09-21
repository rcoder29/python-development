# Goal
# Declare a list [1, 4, 9, 16, 25] or tuple (1, 4, 9, 16, 25) and use the for-loop to print out all values that are even.

mylist = [1, 4, 9, 16, 25]
for x in mylist:
    if x%2 == 0:
        print("Even value - ", x)
    else:
        continue

# create 3 lists and print the values through for construct
names=['Charles', 'John', 'Ryan']
ages=[30,25,32]
emails=['Charles@citadel.com', 'john@citadel.com', 'Ryan@citadel.com']

for i in range (0,3):
    print(names[i], ages[i], emails[i])


# Ask user to enter number 10 times between 1 to 8 and store them in a list
# count numeber of times 5 is entered
count=1
mylist=[]
while(count<=10):
    uval=int(input("Enter a valid number from 1 to 8: "))
    mylist.append(uval)
    count+=1

#print
for i in mylist:
    print(i)
print("Number 5 appeared followig number of times : ", mylist.count(5))


#unix style permission string and print which ones have write permision
permstr=input("Enter Permission String in format of 3 letters as RWX : ")
print("User Entered String ", permstr)
permlist=[]
for c in permstr:
    permlist.append(c)

# print
if permlist[0] == 'w':
    print("User has Write Permission")
if permlist[1] == 'w':
    print("Group has Write Permission")
if permlist[2] == 'w':
    print("Other has Write Permission")


# list comprehension
#Declare a list as in Lab 1 [1, 4, 9, 16, 25]; this time use list comprehension to filter our odd numbers.
mylist=[1, 4, 9, 16, 25]
filterlist=[num for num in mylist if (num%2==0)]
for i in filterlist:
    print(i)
