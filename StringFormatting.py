def print_formatted(number):
    
    # your code goes here
    #get required values
    decimalValues = []
    octalValues = []
    hexValues = []
    binValues = []
    for i in range(number):
        decimalValues.append(i+1)
        hexValues.append(hex(i+1).replace('0x',''))
        octalValues.append(oct(i+1).replace('0o',''))
        binValues.append(bin(i+1).replace('0b',''))
    
        
    lengthBinary = len(binValues[-1])
    
    
    for index,row in enumerate(decimalValues):
        print(str(decimalValues[index]).rjust(lengthBinary), str(octalValues[index]).rjust(lengthBinary), str(hexValues[index]).rjust(lengthBinary).upper(), str(binValues[index]).rjust(lengthBinary))
    