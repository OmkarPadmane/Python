#parrent class
class Employee:
    
    name=""
    ID=""
    details=""
    # def setvalue(self,n,id,d):
    #     self.name=n
    #     self.ID=id
    #     self.details=d
        
    def __init__(self,n,id,d) -> None:
        self.name=n
        self.ID=id
        self.details=d
        
    def display(self):
        print("\n NAME ",self.name)
        print("\n ID ",self.ID)
        print("\n DETAILS ",self.details)

        
# a= Employee()
# n1=input("NAMe:")
# id1=input("ID:")
# d1=input("details:")
# a.setvalue(n1,id1,d1)
#print(a.name)
b= Employee("ANUJ","ab1","mumbai")
b.display()
print(b.name)
