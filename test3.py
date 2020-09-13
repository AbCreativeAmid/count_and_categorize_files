def test3(list):
    sumev = 0
    sumod = 0
    for el in list:
        if(el%2==0):
            sumev += el
        else:
            sumod += el
    return [sumev,sumod]
print(test3([1,2,3,4,5,6]))