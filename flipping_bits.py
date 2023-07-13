def flippingBits(n):
    # Write your code here
    # bin_str = '{:032b}'.format(n)
    binary = bin(n).replace("0b","")
  
    # print(f"converted to binary{binary}")
    # print(bin_str)
    bits = len(binary)*8
    bitted =""
    for i in range(bits-len(binary)):
        bitted= bitted+"0"
    bitted = bitted + binary
    print (bitted)
    # flipped_bitted=""
    # for i in bitted:
    #     if i == "0":
    #         flipped_bitted=flipped_bitted+"1"
    #     else:
    #          flipped_bitted=flipped_bitted+"0"

    # flipped_decimal = int(flipped_bitted,2)
    # print(bitted)
    # print(flipped_bitted)
    # return (int(flipped_decimal))




    
    # Write your code here 
    bin_str = '{:032b}'.format(n) 
    print(bin_str)
    result = []
    for i in bin_str:
        if i =="1":
            result.append("0")
        else:
            result.append("1")
    
    # out = ["0" if i == "1" else "1" for i in bin_str]
    result = "".join(result)
    return int(result,2)

print(flippingBits(2147483647))

