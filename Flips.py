def minFlips(target):
 
    curr = '1'
    count = 0
     
    for i in range(len(target)):
         

        if (target[i] == curr):
            count += 1
             
           
            curr = chr(48 + (ord(curr) + 1) % 2)
     
    return count
print(minFlips("01011"))