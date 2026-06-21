def largest_word(s:str):
    words = s.split()
    return max(words , key=len)

print(largest_word("apple banana cherry blueberries"))