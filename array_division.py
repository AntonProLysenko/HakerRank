def birthday(s, d, m):
    # Write your code here
    ron_squares = 0
    # print(len(s)-1)
    # sumary = 0
    for i in range(0,(len(s))):
        if sum(s[i:i+m]) == d:
                ron_squares += 1

        # print(f'{s[i]} i')
        # print(f'{d} d')
        # print(s[i] == d)
        # if s[i] == d:
        #     sumary= s[i]
        # else:
        #     for j in range(i+1,m):  
        #         sumary = s[i]+s[j]
        #         # print(sum)
        # if sumary == d:
        #     ron_squares+=1
    
    return ron_squares

chcolate =[4]
day =4
month = 1
print(birthday(chcolate,day,month))

