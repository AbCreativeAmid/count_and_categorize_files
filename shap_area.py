def shap_erea(n):
    area = 0
    for i in range(1,(2*n)-2,2):
        area += i
    area = (area*2)+(2*n-1)
    return area
    
n = eval(input("Enter number!:_ "))
while n != 0:
    print(shap_erea(n))
    n = eval(input("Enter number!:_ "))