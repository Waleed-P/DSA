# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

def longest_palindrome(s:str):
    seen = set()
    length = 0
    for i in s:
        if i in seen:
            seen.remove(i)
            length+=2
        else:
            seen.add(i)
    if length %2==0:
        return length+1
    else:
        return length
    
print(longest_palindrome("abccccdd"))