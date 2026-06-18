def palindrome(s:str) -> bool:
    chars = list(s)
    left,right=0,len(s)-1
    while(left<right):
        if chars[left] == chars[right]:
            return True
        left +=1
        right-=1
    return False
def palindrome_slicing(s: str) -> bool:
    return s == s[::-1]

print(palindrome("madam"))
print(palindrome("malayalam"))
print(palindrome("hello"))
print(palindrome_slicing("madam"))
print(palindrome_slicing("malayalam"))
print(palindrome_slicing("hello"))