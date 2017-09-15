#!/usr/bin/python3
x = float(input("enter a number: "))
epsilon = 0.1
num_guesses = 0
ans = 0.0   # ans stands for the guess answer

while ans * ans <= x:
    ans += epsilon        
    num_guesses += 1

print("number of guesses =", num_guesses)
print(ans, "is close to square root of", x)

# the results of entering 10 in this algorithm are as follows:
#number of guesses = 316228
#3.1622800000122493 is close to square root of 10.0


#when enter the number - 12345, number of guesses = 11110806


# try: change the epsilon value to 0.1
# the results of entering 10 in this algorithm are as follows:
#number of guesses = 32
#3.2000000000000015 is close to square root of 10.0
# Comparing to epsilon is in a smaller value, the current one with a larger value
#decrease the number of guesses. Meanwhile, the accuracy is reduced.
