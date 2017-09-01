#initiate two prompts
def main():
    choice = "y"
    while choice.lower() == "y":
        a = input("Please add a number that you'd like to do in a calculation to get the average: ")
        a = float(a)
        b = input("Please add another number in the calculation: ")
        b = float(b)

#calculate the average
        ave = round((a+b) / 2, 2)

        print("Attention! Here is the arithmetic mean of the two numbers you just provided: " + str(ave))
        print()
        choice = input("Continue? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()

