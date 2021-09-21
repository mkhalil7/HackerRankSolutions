def swap_case(s):
    #empty array to hold all the characters
    newWord = []
    
    #go through all the characters
    for c in s:
        #check and reverse case
        if(c.isupper()):
            newWord.append(c.lower())
        else:
            newWord.append(c.capitalize())
    #join letter in the array into the new word        
    return "".join(newWord)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)