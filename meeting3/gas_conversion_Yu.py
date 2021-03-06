
def main():
    choice = "y"
    while choice.lower() == "y":
        num_gallon_gasoline = input("Please enter the number of gallons of gasoline:  ")

#conversion to other measurements

        num_gallon_gasoline = float(num_gallon_gasoline)

#for liters
        num_liters = num_gallon_gasoline * 3.7854
        num_liters = round(num_liters,2)

#for barrels of oil 
        num_barrel_oil = num_gallon_gasoline / 19.5
        num_barrel_oil = round(num_barrel_oil,2)
#for price in U.S. dollars
        price = num_gallon_gasoline * 3.17
        price = round(price,2)
        print()
        print("Attention! The number of gallons of gasoline that you just entered can be converted into other measurements as follows: ")
        print()
        print("Equivalent number of liters: ", num_liters)
        print()
        print("Number of barrels of oil required to produce it: ", num_barrel_oil)
        print()
        print("Price in U.S. dollar: ", "$" + str(price))
        print()
        choice = input("Continue? (y/n): ")
        print()
    print("Bye!")


if __name__ == "__main__":
    main()



