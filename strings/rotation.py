def rotation(s1:str,s2:str)->bool:
    if len(s1) == len(s2) and s2 in (s1 + s1):
        return True
    else:
        return False
    
print(rotation("apple","leapp"))
print(rotation("hello", "llhoe"))