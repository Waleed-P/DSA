list1 = [i for i in range(10)]
print(list1)
list2=["hello" for i in range(6)]
print(list2)
nums=[1,2,3,4,5,6,7,8,9,10]
list3=["even" if i%2==0 else "odd" for i in nums]
print(list3)
list4=["even" if i%2==0 else i for i in nums if i <=8]
print(list4)
list5=[n * n for n in nums]
print(list5)