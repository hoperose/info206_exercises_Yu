#initiate two prompts
a = input("Please add a number that you'd like to do in a calculation to get the average: ")
a = float(a)
b = input("Please add another number in the calculation: ")
b = float(b)

#calculate the average
ave = (a+b) / 2

print("Attention! Here is the arithmetic mean of the two numbers you just provided: " + str(ave))
