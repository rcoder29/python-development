def test_function1(x):
    x=x+1
    print(x)

def list_append(mylist):
    mylist.append("!!!")
    print(mylist)

x=10
test_function1(x)
print(x)

mylist=['a','b']
list_append(mylist)
print(mylist)

# rotate list
# move last element of the list to first
def rotate_list(mylist):
    newlist=mylist.copy()
    newlist[0]= mylist[len(mylist)-1]
    for i in range(0, len(mylist)-1):
        print(i)
        newlist[i+1] = mylist[i]
    return newlist

mylist=[1,2,3,4,5]
print(rotate_list(mylist))


# function that takes a list and variable number of indices
# prints the values of indicies
def funcvarargs(*listargs, **kwargs):
    return kwargs.values()
print(funcvarargs(1,2,3,x=20,y=40,z=25,name="Raghu", value="Citadel"))

# return named, value parameters as dictionary
def funcvarargs1(**kwargs):
    return kwargs.items()
print(funcvarargs1(x=20,y=40,z=25,name="Raghu", value="Citadel"))


# accumulate initial value and sum of each value in tuple
def accumulate(orig, mytuple):
    finalval=orig
    for val in mytuple:
        finalval+=val
    return finalval
print(accumulate(1,(2,3,4,5,6)))

# fibonacci as function with parameter taken to identify upto how many #s to build
def gen_febonacci(count):
    val1, val2 = 0,1
    mylist=[]
    for i in range(1, count+1):
        val1, val2 = val2, val1+val2
        mylist.append(val1)
    return mylist
print(gen_febonacci(10))
print(gen_febonacci(100))
print(gen_febonacci(500))
