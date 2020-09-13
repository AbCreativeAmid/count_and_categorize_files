#this program is for global and casting in python
first = "Abdullah"
second = "AbCreative"
def local_show_names():
    """this function works with local variables"""
    first = "AbCreative is nickname for Abdullah"
    print("in function: ",first)
print ("print"+str(1)+": ",first)
local_show_names()
print("print"+str(2)+": ",first)
print("============= second part ===========")
def global_show_names():
    """this function works with global variables"""
    global second
    second = "AbCreative is nickname for Abdullah Hussaini"
    print("in function: ",second)
print("print"+str(1)+": ",second)
global_show_names()
print("print"+str(2)+": ",second)
