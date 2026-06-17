nums=[1,2,3,4,5,6,7]
evens=0
odds=0
for num in nums:
    if num%2==0:
        evens+=1
    else:
        odds+=1
        
print("odds=>",odds,"evens=>",evens)