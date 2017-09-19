
def sum_digits(n):  #Define a function which takes an int and returns the sum of its (positive value) digits
    '''Returns the sum of all digits (positive value) in the integer'''
    n = abs(n)
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def diff_sum_digits(n): #Define a functon that "wraps" the sum_digits defined previously
    '''Compute the input number minus the sum of digits of input number'''
    temp_val = sum_digits(n)
    ans = n - temp_val
    return ans


def wraps_diff_sum_digits(n):
    while True:
        ans = diff_sum_digits(n)
        digits = len(str(ans))
        if digits > 1:
            n = ans
        else:
            break
    return ans

