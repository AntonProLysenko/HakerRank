def birthday(s, d, m):
    # Write your code here
    result=[]
    for i in range(len(s)):
       j=i+1 
       for j in range(len(s)):
           print(s[i],s[j])
           sum =s[i]+s[j]
           if sum == d:
               result.append(sum)
    return result
           
           





print(birthday([1,2,3,4,5],4,2))