def repeat1(s:str):
    count=dict()
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for key , value in count.items():
        if value == 1:
            return key
    return -1

def repeat2(s:str):
    chars = list(s)
    seen = set()
    for i in range(len(chars)):
        item = chars[i]
        sliced_list = chars[i+1:]
        if item not in sliced_list and item not in seen:
            return item
        seen.add(item)
    return -1
print(repeat1("abcabxd"))
print(repeat2("abcabxd"))