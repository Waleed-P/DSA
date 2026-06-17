def to_lower(s:str):
    result=[]
    for i in s:
        assci_val = ord(i)
        if assci_val >=65 and assci_val <=90:
            result.append(chr(assci_val + 32))
        else:
            result.append(i)
    return "".join(result)

a="HELLO"
print(to_lower(a))