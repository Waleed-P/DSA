def anagram(first_word:str,second_word:str):
    char_count = dict()
    if len(first_word) != len(second_word):
        return False
    for char in first_word:
        char_count[char] = char_count.get(char, 0) + 1
    for char in second_word:
        if char not in char_count or char_count[char]==0:
            return False
        char_count[char]-=1
    return True
    
print(anagram("cat","caat"))