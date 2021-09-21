import textwrap

def wrap(string, max_width):
    partitions = []
    strLen = len(string)   
    i=0
    while(i< strLen):
        partitions.append(string[i:i+max_width])
        i+=max_width
    
    return "\n".join(partitions)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)