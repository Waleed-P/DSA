def reverse(s:str):
    reversed_str =""
    for i in range(len(s)-1,-1,-1):
        reversed_str+=s[i]
    return reversed_str

def reverse2(s:str):
    reversed_string=[]
    for i in range(len(s)-1,-1,-1):
        reversed_string.append(s[i])
    return "".join(reversed_string)
def reverse3(s:str):
    reversed_str =[]
    chars=list(s)
    left,right =0, len(s)-1
    while(left<right):
        chars[left],chars[right]=chars[right],chars[left]
        left+=1
        right-=1
    return "".join(chars)
        
print(reverse("hello"))
print(reverse2("hello"))
print(reverse3("hello"))