#!/usr/bin/python3
x = float(input("enter a number: "))
epsilon = 0.00001
num_guesses = 0
low = 0.0
high = x
ans = (high + low) / 2.0

while high-low >= 2 * epsilon:
    if (ans**2 > x):
        high = ans
    elif (ans**2 < x):
        low = ans
    else:
        break
    ans = (high + low) / 2.0
    num_guesses += 1
print("low =", low, "high =", high)
print("number of guesses =", num_guesses)
print(ans, "is close to square root of", x)

#with the following results, the algorithm took 19 steps.
#the final guess is 3.1622791290283203
#low = 3.1622695922851562 high = 3.1622886657714844
#number of guesses = 19
#3.1622791290283203 is close to square root of 10.0 


#with the following results, the algorithm took 31 to get the square root of 26894
#the final guess is 163.99390397267416
#low = 163.99389771092683 high = 163.9939102344215
#number of guesses = 31
#163.99390397267416 is close to square root of 26894.0

# a problem happens when find the square root of 0.25, since the its
# square root is not in the interval [0, x].
# the method to debug is reassigning the high variable like this: high = max(x, 1.0)
# When the bug is fixed, the results are as follows:
#low = 0.0 high = 1.0
#number of guesses = 0
#0.5 is close to square root of 0.25
