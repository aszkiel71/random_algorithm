from math import log

# ---- This function check whether the requested number is a prime number.
def isPrime(number):
    if abs(number) == 1 or number == 0:
        return False
    for i in range(2, number-1):
        if number % i == 0:
            return False
    return True


# ---- This function returns the number of prime numbers (from zero to the specified one)
def WhatAmount(number):
    if number <= 1:        return 0
    counter = 0
    for i in range(number+1):
        if isPrime(i) == True:
            counter += 1
        if counter + 1 > number/log(number):
            break #TO OPTIMIZE
    return counter

print(WhatAmount(100))