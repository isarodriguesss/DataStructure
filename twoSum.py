def twoSum(array, target):
    for i in range(len(array)):
        for j in range(len(array)):
            if (i != j) and (array[i] + array[j] == target):
                return [i, j]


nums = [2,7,11,15]
target = 9             

print(twoSum(nums, target))