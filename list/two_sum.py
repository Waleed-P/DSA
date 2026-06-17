def two_sum(nums,target):
    seen = set()
    for num in nums:
        if target-num in seen:
            return [target-num,num]
        else:
            seen.add(num)
    return -1

print(two_sum([1,2,3,4,5],9))