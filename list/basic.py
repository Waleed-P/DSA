fruits=["apple","avacado","mango","pinapple","banana"]
a = [0,0,1,1,1,2,2,3,3,4]
b = [1,1,2]
def remove_dup(nums:list):
    left=0
    right=1
    while(right<len(nums)):
        if nums[left] == nums[right]:
            nums.remove(nums[right])
        left+=1
        right+=1
    return nums

print(remove_dup(a))
print(remove_dup(b))

def remove_dup2(nums:list):
    nums= list(set(nums))
    return nums, len(nums)

print(remove_dup2(a))
print(remove_dup2(b))