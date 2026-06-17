def occurance(nums,item):
    count = 0
    for num in nums:
        if num == item:
            count +=1            
    return count

print(occurance([1,2,3,4,5,2,2,3,2,2],2))