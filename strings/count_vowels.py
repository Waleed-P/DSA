a="education"
count=0
vowels = "aeiou"
for i in a:
    if i in vowels:
        count+=1
vowels_count = sum(1 for i in a if i in vowels)
print(count,vowels_count)