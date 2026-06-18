def replace_char(s:str,char:str,new_char:str):
    char_list=list(s)
    for i in range(len(char_list)):
        if char_list[i] == char:
            char_list[i]=new_char
    return "".join(char_list)

print(replace_char("banana","a","@"))