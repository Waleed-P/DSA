def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
        nums[i],nums[minpos]=nums[minpos],nums[i]
    return nums

print(sort([3,2,5,7,2,0]))