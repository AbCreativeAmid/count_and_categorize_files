x = "first"
def parent():
    x = "second"
    def child():
        nonlocal x
        x = "third"
        def child2():
            global x
            x = "fourth"
            print(x)
        child2()
        print(x)
    child()
    print(x)
parent()
print(x)