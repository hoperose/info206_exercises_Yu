#Module-palindrome: Reverse the name order and also the letters order within each name

def main():
    while True:
        entry = input("Please enter your full name: (i.e., firstname, middlename, and lastname)")
        revname = entry.lower()[::-1]
        if entry.lower() == revname:
            print("Palindrome!")
        else:
            print(revname)

        
if __name__ == "__main__":
    main()




