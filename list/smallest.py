nums = [10,20,30,50,-100,150,-50,-500]
smallest = nums[0]
for num in nums:
    if smallest > num:
        smallest = num
print(smallest)