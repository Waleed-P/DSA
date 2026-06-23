def prefix(words:list):
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix
        
words=["flower", "flow", "flight"]
print(prefix(words))