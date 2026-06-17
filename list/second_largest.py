def second_largest(nums):
    unique_nums = list(set(nums))
    unique_nums.sort() 
    return unique_nums[-2]

print(second_largest([100,800,600,1,2,3,4,5,-50,-32]))