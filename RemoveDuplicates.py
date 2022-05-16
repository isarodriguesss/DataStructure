def removeDuplicates(nums):
    j = 1
    for i in range(1,len(nums)):
        if nums[i-1] != nums[i]:
            nums[j] = nums[i]
            j += 1
    return nums
    

nums = [1,1,2]
print(removeDuplicates(nums))

#Complexity = O(N)