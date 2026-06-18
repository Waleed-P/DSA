def count_words(s:str)->int:
    count = s.split()
    return len(count)

print(count_words(" hello world "))
print(count_words(" "))
print(count_words(""))