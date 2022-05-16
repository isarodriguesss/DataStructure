def maxSubarray(nums):
    sum = nums[0]
    max_sum = nums[0]
    for i in range(1,len(nums)):
        print(sum, max_sum)
        if nums[i] > sum+nums[i]:
            sum = nums[i]
        else: 
            sum += nums[i]
        if max_sum < sum:
            max_sum = sum    
    return max_sum

nums = [5,4,-1,7,8]

print(maxSubarray(nums))
