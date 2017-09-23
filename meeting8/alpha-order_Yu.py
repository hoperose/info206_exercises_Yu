#create a loop to search for the common letter between two string entries
w1 = input("Please enter the first word: ")
w2 = input("Please enter the second word: ")
cl = list(set(w1) & set(w2))
scl = ''.join(sorted(cl))
print("Letters in common: ", scl)

