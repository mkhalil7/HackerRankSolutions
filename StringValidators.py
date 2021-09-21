if __name__ == '__main__':
    s = input()
        
#intial values
    isAlphanumeric = False
    isAlphabetical = False 
    isDigit = False
    isLower = False
    isUpper = False

#checking every character
    for c in s:
        if(c.isalnum()):
            isAlphanumeric = True
        if(c.isalpha()):
            isAlphabetical = True
        if(c.isdigit()):
            isDigit = True
        if(c.islower()):
            isLower = True
        if(c.isupper()):
            isUpper = True

#printing
    print(isAlphanumeric)
    print(isAlphabetical)
    print(isDigit)
    print(isLower)
    print(isUpper)



