
# print(stock_arr)

# checkr = 0

def miniMaxSum(arr):
    # Write your code here
    checkr = 0
    arr_of_sums=[]
    
    def findSumOfFour(arr):
        nonlocal checkr
        sum_of_loop=0
        for val in arr:
            # global sum_of_loop
            sum_of_loop += val
        sum_of_loop -= arr[checkr] 
        checkr+=1
        arr_of_sums.append(sum_of_loop) 

        # return sum_of_loop
    
    for i in range(5):
        findSumOfFour(arr)
        # print( arr_of_sums)

    print(f"MIN:{min(arr_of_sums)} MAX:{max(arr_of_sums)}")

stock_arr = [10,20,30,40,50]
miniMaxSum(stock_arr)



def add_ten_percents(price):
    price+=(10*price)/100
    return price
print(add_ten_percents(100))


# print("Hello World!")