def twoSum(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(str(i))
                result.append(str(j))
    return result