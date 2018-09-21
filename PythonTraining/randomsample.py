# Ask users to enter a random number in the range and keep going until user guesses the right number

import random

# get range
start = int(input("Enter start of range : "))
end = int(input("Enter end of range : "))

# iterate over getting input from user and checking
while(True):
    print("Range to uesr for Random number ", start, end)
    userinput = int(input("Enter a random number :"))
    randnum = random.randint(start, end)
    if userinput == randnum :
        print("Congratulations, You guessed it Ready!!!, program exiting...")
        break
    else:
        print("Sorry, wrong guess, try it again....", userinput, randnum)

# end of the program
print("End of the program")
