def find_permut(str):
   
    list_str = list(str)
    i = len(str)-2
    j = len(str)-1

    while  i>=0 and list_str[i] >= list_str[i+1]:
        i-=1 

    while j>0 and list_str[j] <= list_str[i]:
        j-=1

    list_str[i], list_str[j] = list_str[j], list_str[i]

    next_prem = ''.join(list_str)
    
    if i<0:
        print("No next Permutation possible")
    else:
        print(next_prem)
        find_permut(next_prem)

    # return next_prem

    




str = "aabc"
find_permut(str)

