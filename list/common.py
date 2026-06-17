a = [1,2,3,4]
b = [3,4,5,6]

def commmon(list1,list2):
    result=[]
    for num in list1:
        if num in list2 and num not in result:
            result.append(num)
    return result

print(commmon(a,b))