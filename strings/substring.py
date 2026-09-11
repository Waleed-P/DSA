def substring(haystack:str,needle:str):
    if not needle : return 0
    for char1 in haystack:
        if char1 == needle[0]:
            