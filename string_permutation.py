def next_permutation(s):
    # Convert the input string to a list of characters
    arr = list(s)
    lenth = len(arr)
    i = lenth - 2
     
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
    rev(arr, i+1, lenth-1)
    return ''.join(arr)
 
 # Function to reverse the array
def rev(arr: list, start: int, end: int) -> None:
    while start < end:
        swap(arr, start, end)
        start += 1
        end -= 1
 # Function to swap two numbers
def swap(arr: list, i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
 

s = "abac"
print(next_permutation(s))