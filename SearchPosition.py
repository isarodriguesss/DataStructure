def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return i
        elif target > nums[len(nums)-1]:
            return len(nums)

nums = [1,3,5,6]
target = 7

print(searchInsert(nums, target))
