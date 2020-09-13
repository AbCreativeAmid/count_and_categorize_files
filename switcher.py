def testSwitch(arg):
    switcher = {
        0: "It is just zero",
        1: "It is just one",
        2: "It is just two",
        3: "It is just three"
    }
    return switcher.get(arg,"nothing")
x = 0
while(x<4):
    print(testSwitch(x))
    x+=1
from config import *
print(config.name)
