def compress_str(s:str):
    count = 0
    str_list=[]
    for char in s:
        if char not in str_list:
            if count !=0:
                str_list.append(count)
                count=0
            str_list.append(char)
            count = 1
        else:
            count+=1
    if count !=0:
        str_list.append(count)
        count=0
    return str_list

def compress_str2(s:str):
    left=0
    right=1
    count=1
    result=[]
    while(right<len(s)):
        if s[left] == s[right]:
            count+=1
        else:
            result.append(s[left])
            result.append(str(count))
            count=1
        left+=1
        right+=1
    result.append(s[left])
    result.append(str(count))
    return "".join(result)
print(compress_str("aaabbccccdddddd"))
print(compress_str2("aaabbccccdddddd"))
