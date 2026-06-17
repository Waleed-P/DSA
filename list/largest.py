nums=[10,500,30,40,50,60,70]
largest=nums[0]
for num in nums:
    if largest < num:
        largest = num
print(largest)