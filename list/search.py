def search(nums,item):
    for i,num in enumerate(nums):
        if num == item:
            return i
    return -1
print(search([1,2,3,4,5],3))