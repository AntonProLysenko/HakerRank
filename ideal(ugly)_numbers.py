def getIdealNums(low,high):
    result=0
    for i in range(low, high+1):
        if i<=0:
            return False
        while i % 5 == 0:
            # print(f'in while5 {i}')
            i=i/5
        while i%3 == 0:
            # print(f'in while3 {i}')
            i = i/3
        if i == 1:
            result+=1
    
    return result

print(getIdealNums(221 ,225))
