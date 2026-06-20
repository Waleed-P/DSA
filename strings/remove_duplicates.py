# input = "programming" , output = progamin
def remove_duplicate(s:str)->str:
    charecter_list = list(s)
    result = list()
    for i in charecter_list:
        if i not in result:
            result.append(i)
    return "".join(result)

def remove_duplicate2(s:str):
    result=[]
    seen=set()
    for char in s:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return "".join(result)

def remove_duplicate3(s:str):
    return "".join(set(s))

def remove_duplicate4(s:str):
    charecter_count=dict()
    for char in s:
        if char in charecter_count:
            charecter_count[char]+=1
        else:
            charecter_count[char]=1
    return "".join(charecter_count.keys())

print(remove_duplicate("programming"))
print(remove_duplicate2("programming"))
print(remove_duplicate3("programming"))
print(remove_duplicate4("programming"))