def test2(year):
    century = year//100
    return century+1 if year%100 == 0 or year%100>0 else century
print(test2(50))
print(test2(102))
print(test2(200))
