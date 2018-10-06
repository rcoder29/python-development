# Given a two dimensional array of numbers sorted both row and column wise
# find number of negative numbers in the 2D array
# Simple Solution - Scan through MxN matrix to find if number is < 0 and increment counter
# Optimal Solution - Start at max index in row 1 and walk backwards to find first -ve number, once it is found, identify number
# of elements upto that point in that row and step down to next row and same column and move right or left depending on if that number is 
# +ve or -ve and repeat this process until last row is reached
# this will be with order of complexity of M+N
