def test(num1,num2):
    return num1+num2 if num1*num2 >= 100 else 0
print("first:",test(2,49))
print("second:",test(2,69))