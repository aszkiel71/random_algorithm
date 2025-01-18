# 1 - 2x + 3x^2 - 4x^3 + ... = 1/(1+x)^2 at least for absolute values |x| < 1
# dynamic programming

def series(n):
    values_array = [0]*n
    sign = 1
    power = 1
    for i in range(n+1):
        values_array[i] = sign*i*
        sign *= -1