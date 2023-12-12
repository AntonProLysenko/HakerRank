# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

def sockMerchant(n, ar):
    output = []
    
    #Running over all socks by each
    for i in range(0, n):
        #If there are more that 1 sock and we don't have it in output we push
        if ar.count(ar[i])>1 and ar[i] not in output:
            #In case if we have more than one pair of same sock we push multiple time(count/2) declares amount of pairs in case if not even we flooring pait amnt
            for j in range(0, ar.count(ar[i])//2):
                output.append(ar[i])
    return(len(output))


basket = [10, 20, 20, 10, 10, 30, 30, 40]

print(sockMerchant(len(basket), basket))