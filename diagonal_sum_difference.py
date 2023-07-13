def diagonalDifference(arr,n): 
# Write your code here
    # diagonal_sum1=0
    # diagonal_sum2=0
    # # print("here")



    # top = arr[0]
    # mid = arr[1]
    # bottom = arr[-1]

    # diagonal_sum1 = top[0]+mid[1]+bottom[2]
    # diagonal_sum2 = top[2]+mid[1]+bottom[0]

    left_diag=0
    right_diag=0
    for i in range(n): 
        right_diag+=arr[i][n-i-1]
        left_diag+=arr[i][i]
    result = left_diag-right_diag
    if result<0:
        result = -result
    return result

    # for i in arr:
    #     print(i)
    #     diagonal_sum1+=i[0]
    #     diagonal_sum2 += i[-1]
    #     if 
        #     for j in i:
        #         if j[0]:
        #             diagonal_sum1+=j
        #             print(f"sum1{diagonal_sum1}")
        #         elif j[2]:
        #             diagonal_sum2+=j
        #             print(f"sum2{diagonal_sum2}")
        # elif i[1]:
        #     diagonal_sum1+= i[1]
        #     diagonal_sum2+=i[1]
        #     print(f"sum1{diagonal_sum1} sum2{diagonal_sum2}")
        # elif i[2]:
        #     for j in i:
        #         if j[0]:
        #             diagonal_sum2+=j
        #             print(f"sum1{diagonal_sum2}")
        #         elif j[2]:
        #             diagonal_sum1+=j  
        #             print(f"sum1{diagonal_sum1}")
    diff = diagonal_sum1-diagonal_sum2
    if diff <0:
        diff = -diff
    return(diff)
                


the_arr = [[11,2,3],[4,5,6],[10,8,-12]]
print(diagonalDifference(the_arr, len(the_arr)))