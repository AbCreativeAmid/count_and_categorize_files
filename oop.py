class first_class():
    name = ""
    last_name = ""
    def __init__(self,name,last_name):
        self.name,self.last_name=name,last_name
    def hello(self):
        print("Hello! Good morning")
    def hello_someone(self,str):
        print("Hello {} Good Morning {}".format(str,str))
class child_class(first_class):
    def hello3(self):
        print("Hello Third")

c = first_class("Adbdulah","Hussaini")
print(c.name)