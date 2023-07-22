# inheritance 

class Father:
    def __init_(self,name):
        self.name = "Hello"
    
    def ReadWell(self,a,b):   # class attributes 
       
       return a + b + self.name
    
    def printNumber():
        pass

class Mother:
    def WriteWell(x,y):
        return x * y
    
    def printStrings():
        pass 

class Child(Father,Mother):
    def __init__(self):
        pass
    
    def ListenMore():
        print("printing Argunemnts")



print(Child.WriteWell(10,15))
print(Child.ReadWell(10,15))



