def append_at_middle(string1,string2):
    center = len(string1)//2
    result = string1[:center]+string2+string1[center:]
    return result
print(append_at_middle("Ault","kelly"))