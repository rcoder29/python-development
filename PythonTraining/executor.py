'''
Code for lab around functional programming
'''

'''
The Command Pattern presents a way of encapsulating an operation into an object that can be passed around between objects, managed, sequenced, scheduled and executed as required. It seperates the instantiation of an operation from the execution of that operation, and thus allows operations to be persisted, ressurected as well as offering the option of executing operations remotely.

The command pattern has the following constituent parts:

Command Executor: This type is responsible for managing the collection and execution of commands. That is, the executor knows how to execute commands.

Command: Represents the behaviour to be executed by the command executor.

Create an Executor class. This call should accept a command to run (and assume that it is a callable object - in this case a function). It should execute the command when requested. It should also add the command to a history of commands, so that all commands that have been supplied can be re-run. For debugging purposes, the executor should have a name and be able to be printed meaningfully.

An example of the usage might be:
def main():
	e = Executor("executor")
	e.execute(doit)
	e.execute(dothis)
	e.execute(lambda: print('lambda'))
	print ('-' * 25)
	e.rerun()
	print (e)

if __name__ == '__main__':
	main()
'''

from abc import ABCMeta
from threading import Thread
from time import sleep
import time
from  random import randrange

# futures for thread pool executor
from concurrent.futures import ThreadPoolExecutor

# logging decorator
def logger(func):
    def wrapped(self, func):
        st = time.time()
        func()
        ed = time.time()
        print("Total time taken to execute the function - ", func.__name__, (ed - st))

    return wrapped


# Logger mixin
# mix in is nothing but a certain behavior or interface that can  be used by classes that inherit from it!
class loggerMixIn():
    def log_message(self):
        print("Time now - ", time.time())


# executor class
class Executor(loggerMixIn, metaclass=ABCMeta):
    def __init__(self, name):
        # initialize executor object
        self.commandhistory = []
        self.name = name
        self.pool = ThreadPoolExecutor(3)

    # commented out to test the mixin logger
    # @logger
    def _localExec(self, func):
        #sleep(random.randrange(4)) # random sleep to demonstrate the threads running in random!
        func()

    def execute(self, func):
        # add to list
        self.commandhistory.append(func)

        # start a new thread to run the execution of the underlying function
        t1 = Thread(self._localExec(func))
        print ("invoke running in thread -- ", t1.name)
        t1.start()

    def executeAsFuture(self, func, *args, **kwargs):
        # run the function as a future, so it invokes a future and returns it so it doesnt block for the call
        # add to list
        self.commandhistory.append(func)

        # return a future
        future1 = self.pool.submit(func, *args, **kwargs)
        return future1

    def rerun(self):
        # loop through all previous commands and execute them!
        print("!!!! Rerunning all the commands passed to executor before!!!!")
        for f in self.commandhistory:
            self._localExec(f)


# Processor class to demo the virtual sub class concept
# processor class implement same functions as Executor class but has no inheritance relation to the Executor
# later in the lab it will be registered to be virtual sub class
class Processor(loggerMixIn):
    def __init__(self, name):
        # initialize executor object
        self.commandhistory = []
        self.name = name

    # commented out to test the mixin logger
    # @logger
    def _localExec(self, func):
        func()

    def execute(self, func):
        # add to list
        self.commandhistory.append(func)
        self._localExec(func)

    def rerun(self):
        # loop through all previous commands and execute them!
        print("!!!! Rerunning all the commands passed to executor before!!!!")
        for f in self.commandhistory:
            self._localExec(f)


class InvalidExecutorType(Exception):
    '''
    Custom exception class to raise when input is not of type Executor
    '''

# Invoker bridge class
class Invoker():
    def __init__(self, e):
        if (isinstance(e, Executor)):
            self.__myexec = e
        else:
            raise InvalidExecutorType("Invalid Executor type passed!!")

    def run(self, func):
        self.__myexec.execute(func)

    def rerun(self):
        self.__myexec.rerun()

# sample test functions
def printHello():
    print("Hello")


def printHelloName():
    print("Hello Raghu")

def addTwoNumbers(a,b):
    sleep(5)
    return a+b

def subtractTwoNumbers(a,b):
    sleep(5)
    return a-b

# main usage
def main():
    e = Executor("executor")
    e.execute(printHello)
    e.execute(printHelloName)
    e.execute(lambda: print('lambda'))
    e.log_message()
    print('-' * 25)
    e.rerun()
    print(e)

    # test for virtual sub class concepts
    p = Processor("processor")
    print(issubclass(Processor, Executor))
    print(isinstance(p, Executor))
    Executor.register(Processor)
    # check after registering processor as virutal sub class
    print(issubclass(Processor, Executor))
    print(isinstance(p, Executor))
    print(p)

    # Using invoker redirection
    # Define an Invoker class that takes an executor and acts as a bridge between the commands and the executor.
    # Check that the executor passed to it is a type of Executor - if not, throw an exception.
    print("Trying this through Invoker Concept, using executor .....")
    i = Invoker(e)
    i.run(printHello)
    i.run(printHelloName)
    i.run(lambda: print('lambda'))
    print('-' * 25)
    i.rerun()

    # try the same now by passing Processor!
    # try running this with and without commenting the register method above to see the exception get throwsn on this method call!
    print("Trying this through Invoker Concept, using Processor .....")
    i = Invoker(p)
    i.run(printHello)
    i.run(printHelloName)
    i.run(lambda: print('lambda'))
    print('-' * 25)
    i.rerun()

    # use futures
    future1 = e.executeAsFuture(subtractTwoNumbers, 2,10)
    future2 = e.executeAsFuture(addTwoNumbers,2,10)
    print('Future1 - ', future1.result())
    print('Future2 - ', future2.result())
    print ("!! Done with Futures !!")

# test out the executor class
if __name__ == '__main__':
    main()
