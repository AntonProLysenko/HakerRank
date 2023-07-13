def strings_xor(s, t):
    
    xor_result=""
    
    for i in range(len(s)):
        if s[i]==t[i]:
            xor_result+="0"
        else:
            xor_result+="1"
    return xor_result


print(strings_xor("0101","1101"))




raitings = [4.3, 3.1, 5, 1.1]

recomended = [rate>4 for rate in raitings ]
print(recomended)