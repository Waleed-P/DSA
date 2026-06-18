def charecter_frequency(s:str,char:str) -> int :
    pointer =0
    count =0
    while(pointer<len(s)):
        if s[pointer] == char:
            count+=1
        pointer+=1
    return count

print(charecter_frequency("hello","l"))