#lower case = 97 to 122
# upper case = 65 to 90
def to_upper(s:str):
    result=[] 
    for i in s:
        ascii_value=ord(i)
        if ascii_value >=97 and ascii_value <=122:
            result.append(chr(ascii_value - 32))
        else:
            result.append(i)      
    return "".join(result)

        
a="Hello"
print(to_upper(a))
