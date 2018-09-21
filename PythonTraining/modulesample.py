'''
Sample Module for testing purpose
'''

def module_function1():
    print("I am in module function1")

def module_function2():
    print("I am in module function2")

def main_function():
    print("this is body of the main function of the module!!")

# private functions can be coded with notation of method name starting with _ prefix
# any usage of the private functions in the form of _prefix should be avoided
def _module_function1_internal():
    print("this is internal impl, and not directly supposed to be called!!")

if __name__ == "__main__":
    print("I am run as main module!!")
    main_function()
else:
    print("I am run as a module!!")
