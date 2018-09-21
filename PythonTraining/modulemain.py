'''
This is the main program that is going to call the modulesample to test out the module funcitonality
'''

# shows variations of usage!
import modulesample as mod1
# import modulesample
# from modulesample import *
# from modulesample import module_function1

# call functions of the module
mod1.module_function1()
mod1.module_function2()

# print module name and doc string
print(mod1.__name__)
print(mod1.__doc__)


