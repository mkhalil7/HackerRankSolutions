if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    #creating the tuple
    t = tuple(integer_list)
    #printing the hash
    print( hash(t))