# 283. Move Zeroes
# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
nums = [0,1,0,3,12]
def move_zeros(nums:list):
    left = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i],nums[left] = nums[left],nums[i]
            left+=1
    return nums
        

print(move_zeros(nums))