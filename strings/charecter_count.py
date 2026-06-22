def char_count(s:str):
    count = dict()
    for char in s:
        count[char] = count.get(char, 0)+1
    return count

print(char_count("banana"))