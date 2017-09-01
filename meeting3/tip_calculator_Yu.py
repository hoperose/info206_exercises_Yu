def main():
    choice = "y"
    while choice.lower() == "y":
        price = input("Enter the price of a meal: $")

        price = float(price)
        tip = round(price * 0.16,2)
        total = round(price + tip,2)

        print("A 16% tip would be ", "$" + str(tip))
        print("The total including tip would be ", "$" + str(total))

        print()
        choice = input("Continue? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()
