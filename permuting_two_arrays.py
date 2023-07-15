def twoArrays(k:int, A:list, B:list):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    checkr = []
    for i in range(len(A)-1):
        print(A[i],B[i])
        if A[i]+B[i]>=k:
            checkr.append(True)
        else:
            checkr.append(False)
    if False in checkr:
        return"NO"
    else:
        return"YES"
    
print(twoArrays(4,[2,0,1], [3,4,3]))