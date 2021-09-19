if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(0,N):
        userInput = input().split()
        if userInput[0] == "print":
            print(arr)
        elif userInput[0] == "insert":
            arr.insert(int(userInput[1]),int(userInput[2]))
        elif userInput[0] == "remove":
            arr.remove(int(userInput[1]))
        elif userInput[0] == "pop":
            arr.pop()
        elif userInput[0] == "append":
            arr.append(int(userInput[1]))
        elif userInput[0] == "sort":
            arr.sort()
        else:
            arr.reverse()
            
            