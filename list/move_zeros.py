def move_zeros(nums):
    left = 0
    right= len(nums)-1
    while(left<right):
        if nums[left] == 0 and nums[right] !=0:
            nums[left] = nums[right]
            nums[right] = 0
        left +=1
        right -=1
    return nums
print(move_zeros([1,0,2,0,3,0]))