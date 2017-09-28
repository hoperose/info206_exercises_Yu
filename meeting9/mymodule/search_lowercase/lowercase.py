def any_lowercase1(s):
    '''this code is able to check whether a lowercased letter
       exists in the given string. It returns True if any letter
       in the string is lowercase'''
    for c in s:
        if c.islower():
            return True
        else:
            return False

##

def any_lowercase2(s):
    '''this code is not able to check a string compose of
       all uppercases letters is "False"'''
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
    
##

def any_lowercase3(s):
    '''this code is not able to check any lowercased letter
       exit among a bunch of uppercased letters. It only
       checks all letters are lowercase'''
    for c in s:
        flag = c.islower()
    return flag

##

def any_lowercase4(s):
    '''this code is able to check whether a lowercased letter
       exists in the given string. It returns True if any letter
       in the string is lowercase'''
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

##

def any_lowercase5(s):
    '''this code is only able to check whether all letters
       in the given string are lowercase. It fails in checking
       a combination of lowercase letters and uppercase letters'''
    for c in s:
        if not c.islower():
            return False
    return True

##
def main():
    s = "Hello World!"
    for c in s:
        if 'c'.islower():
            print(s)
        else:
            print("False!")

if __name__ == "__main__":
    main()

    
##
def main():
    s = "Hello World!"
    for c in s:
        flag = c.islower()
        return flag

if __name__ == "__main__":
    main()
