a=[1,2,3,4]
def rotate(nums):
    left=len(nums)-2
    right=len(nums)-1
    print(left,right)
    while(left>=0):
        temp=nums[right]
        nums[right]=nums[left]
        nums[left]=temp
        left-=1
        right-=1
    return nums

print(rotate(a))
b=[1,2,3,4]
print(b[-1:]+b[:-1])