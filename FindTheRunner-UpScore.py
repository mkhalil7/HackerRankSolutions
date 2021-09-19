
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #remove duplicates
    arr = list(dict.fromkeys(arr))
    #sort the array
    arr_sort = sorted(arr,reverse=True)
    #print second element
    print(arr_sort[1])