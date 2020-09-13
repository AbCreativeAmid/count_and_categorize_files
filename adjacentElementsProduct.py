def adjacent_element_product(list):
    larg = list[0]*list[1]
    for i in range(1,len(list)-1):
        new_large = list[i]*list[i+1]
        if new_large>larg:
            larg = new_large
    return larg
a = [5, 1, 2, 3, 1, 4]
print(adjacent_element_product(a))