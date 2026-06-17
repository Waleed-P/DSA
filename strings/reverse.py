def reverse(s:str):
    reversed_str =""
    for i in range(len(s)-1,-1,-1):
        reversed_str+=s[i]
    return reversed_str

print(reverse("hello"))