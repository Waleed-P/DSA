a = [1,2,3]
b = [4,5,6]

def merge(list1,list2):
    for item in list2:
        list1.append(item)
    return list1

def merge2(list1,list2):
    return list1+list2

def merge3(list1:list,list2:list):
    return list1.extend(list2)
print(merge2(a,b))
