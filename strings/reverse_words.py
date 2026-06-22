def reverse_word(s:str):
    words = s.split()
    return " ".join(words[::-1])

print(reverse_word("python is easy"))