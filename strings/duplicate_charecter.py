def duplicate_charecter(s:str):
    dup=set()
    result=set()
    for i in s:
        if i in dup:
            result.add(i)  
        else:
            dup.add(i)
    return result

print(duplicate_charecter("annamma"))