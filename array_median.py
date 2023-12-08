def list_median(arr):
    arr.sort()
    return arr[len(arr)//2]

list = [4,1,2,3,5]
print(list_median(list))