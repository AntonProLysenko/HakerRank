
def removeElement(nums, val):
    result = []
    for i in nums:
        print(f"in for {i}")
        if i!=val:
            print(f"in if {i}")
            result.append(i)
            # nums.remove(i)
            # print(nums)
    print (nums)
    print(result)

removeElement([0,1,2,2,3,0,4,2], 2)
