# 2460. Apply Operations to an Array
# Example 1:

# Input: nums = [1,2,2,1,1,0]
# Output: [1,4,2,0,0,0]


def operation(nums:list):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0
    left=0
    for i in range(len(nums)):
        if nums[i] !=0:
            nums[i],nums[left]=nums[left],nums[i]
            left+=1
    return nums
print(operation([1,2,2,1,1,0]))

# [1,4,2,0,0,0]