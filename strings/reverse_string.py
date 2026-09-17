# 344. Reverse String
# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

s = ["h","e","l","l","o"]
def rev(s:list):
    left = 0
    right = len(s)-1
    while(left<right):
        s[left], s[right] = s[right], s[left]
        left+=1
        right-=1
    return s
print(rev(s))