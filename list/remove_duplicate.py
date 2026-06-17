def duplicate(my_list):
    return list(dict.fromkeys(my_list))


print(duplicate([1,2,3,4,5,5]))