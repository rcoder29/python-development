def multiply(a, b):
    ''' given two numbers return mutiplied value of the two using sum'''

    if isinstance(a, str) or isinstance(b, str):
        raise TypeError('Please provide a number as input..')

    if a is None or b is None:
        return None
    if a is 0 or b is 0:
        return 0

    # to deal with -ve numbers
    sign_val = 1
    if a < 0 or b < 0:
        sign_val = -1
    if a < 0 and b < 0:
        sign_val = 1
    a = abs(a)
    b = abs(b)

    # use a to loop
    sum = 0
    for i in range(a):
        sum += b

    return sum * sign_val


if __name__ == '__main__':
    print('Multiply 2,5 - ', multiply(2,5))
    print('Multiply 2,0 - ', multiply(2, 0))
    print('Multiply 2,None - ', multiply(2, None))
    print('Multiply -10,5 - ', multiply(-10, 5))
    print('Multiply -10,-5 - ', multiply(-10, -5))
    print('Multiply "BAD INPUT",-5 - ', multiply("BAD INPUT", -5))
