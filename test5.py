def test5(list):
    return [el for el in list if type(el)==type(12)]
print(test5([1,'a','b','c','d',15,12]))