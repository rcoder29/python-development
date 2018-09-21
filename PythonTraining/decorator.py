
def logger(func):
    def inner():
        print('calling ', func)
        func()
        print('called ', func)
    return inner

def target():
    print('In target function')

@logger
def target1():
    print('In target function')

if __name__ == '__main__':

    # using explicit calling
    wrapped=logger(target)
    wrapped()

    # using implicit calling
    target1()

