

# define the "multiply" function
def multiply (ListNum = None):
    ''' Multiply all the items
        in the list-ListNum '''
    x = ListNum
    if ListNum is None:
        x = input('Please provide a list to add: ')
        x = x.split(',')
        x = [ int(item.strip()) for item in x]
    ans = 1
    for i in x:
         ans *= i
    return ans
            
              


# define the "addify" function
def addify (ListNum = None):
    ''' Add all items in
        the list-ListNum '''
    x = ListNum
    if ListNum is None:
        x = input('Please provide a list to add: ')
        x = x.split(',')
        x = [ int(item.strip()) for item in x]
    ans = 0
    for i in x:
        ans += i
    return ans

# Verification of "functions are really just objects!"
>>> print(type(multiply))
<class 'function'>
>>> print(type(addify))
<class 'function'>
