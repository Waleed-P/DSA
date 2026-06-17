def sorted(nums:list):
    left=0
    right=1
    while(right<len(nums)-1):
        if nums[left]>nums[right]:
            return False
        left+=1
        right+=1     
    return True
print(sorted([10,2,3,4,5]))