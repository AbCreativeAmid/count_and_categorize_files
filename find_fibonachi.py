def check_for_fibonacci(arg):
    x1 = 0;
    x2 = 1;
    fibonacci = [x1,x2]
    while x1+x2 <= arg:
        temp = x2
        x2 = x1+x2
        x1 = temp
        fibonacci.append(x2)
    return arg in fibonacci
x = eval(input("Enter the number!"))
result = check_for_fibonacci(x)
if result:
    print("Yes it is fibonacci")
else:
    print("No it is not fibonacci")