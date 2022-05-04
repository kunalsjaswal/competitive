#creating class
class myclass1:
    x=10

obj1=myclass1()  #object of class: it can access ecry var of class
print(obj1.x)

# __init__ function is same as constructor

class intro():
    def __init__(self,name,age):
        self.name=name   #self.name=this.name in c++
        self.age=age

obj2=intro("kunal",21)
print(f"name: {obj2.name}")
print(f"age :  {obj2.age}")

class intro2():
    def __init__(self,name,age):
        self.name=name   #self.name=this.name in c++
        self.age=age

    def output(self):
        print(f"my name is {self.name} and age is {self.age}")

obj3=intro2("kunal",21)
obj3.output()
