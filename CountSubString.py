def count_substring(string, sub_string):
    len_sub_string = len(sub_string)
    len_string = len(string)
    cnt = 0
    for i in range(0,len_string - len_sub_string +1):
        if(string[i:i+len_sub_string] == sub_string):
           cnt = cnt +1 
    
    return cnt 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)