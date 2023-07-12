def next_permutation(s):
    # Convert the input string to a list of characters
    arr = list(s)
    lenth = len(arr)
    i = lenth - 2


    # def rev(arr, start, end):
    #     while start < end:
    #         temp_memo = arr[start]
    #         arr[start] = arr[end]
    #         arr[end] = temp_memo
    #     start += 1
    #     end -= 1
    #     print(f"in fu{arr}")
    #     return arr

     
    # Find the largest index i such that arr[i] < arr[i+1]
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
     # If no such index exists, return "No next Permutation"
    if i < 0:
        return "No next Permutation possible"
    

    j = lenth - 1
     # Find the largest index j such that arr[i] < arr[j]
    while j >= 0 and arr[j] <= arr[i]:
        j -= 1
    # Swap arr[i] and arr[j]
    arr[i], arr[j] = arr[j], arr[i]
    # Reverse the sublist arr[start:end+1]
    # rev(arr, i+1, lenth-1)
    return ''.join(arr)
 
 # Function to reverse the array

 

s = "aabc"
print(next_permutation(s))




# if s[-2]>s[-1]:
#     print("Pre last one is more")
# else:
#     print("Pre last one is less")