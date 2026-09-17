# 796. Rotate String

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false

def rotate_detect(s:str,goal:str):
    double_str = s+s
    return len(s) == len(goal) and goal in double_str

print(rotate_detect("m","f"))
print(rotate_detect("abcd","cdab"))