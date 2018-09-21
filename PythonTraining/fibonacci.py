# print first 20 fibonacci numbers
# definition of fibonacci number

val1=1
val2=1
count=2

# append first two numbers
fibnumbers=[]
fibnumbers.append(val1)
fibnumbers.append(val2)

# loop to print first 15 fibonacci numbers
while(count <= 15):
    tmp = val2
    val2 = val1+val2
    val1 = tmp
    count+=1
    fibnumbers.append(val2)

# print the list when the loop is complete!
print('First 15 fib numbers')
for i in fibnumbers :
    print(i)
