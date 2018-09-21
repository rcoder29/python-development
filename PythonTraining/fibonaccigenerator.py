# build a generator for febonacci sequence
# It should return one value ata a time using the yield operation

def febonacci():
    val1 = 1
    yield val1
    val2 = 1
    yield val2
    while True:
        tmp = val2
        val2 = val1 + val2
        val1 = tmp
        yield val2


def febonacciRecursive(val1, val2):
    if (val1==1 & val2 == 1):
        yield val1
        yield val2
    tmp = val2
    val2 = val1 + val2
    val1 = tmp
    yield val2
    if (val2 > 20):
        return
    else:
        yield from febonacciRecursive(val1, val2)


# print the list when the loop is complete!
if __name__ == '__main__':
    print('Printing Fibonacci numbers using generator!!')
    for i in febonacci() :
        print(i)
        if i > 20:
            break

    print("Using Recursive  ...")
    for i in febonacciRecursive(1,1) :
        print(i)
