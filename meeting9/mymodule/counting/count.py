from collections import Counter

def main():
    entry = input("Please enter a word or a sentence: ")
    wordsList = entry.lower().split()
    count = Counter()
    for words in wordsList:
        for letters in words:
            count[letters] += 1
    print(count)


if __name__ == "__main__":
    main()

#entry is "Hello World!"
#the output is Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1})
