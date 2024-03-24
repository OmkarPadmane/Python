# 1)
# Addition/Squaring/exponenation should be done as part of single function named 
# "my_calculator"
# which takes in type of operation, number1,number2 as input 
# and outputs the answer based on the operation
# We need to keep executing my_calculator function 
# untill user choose to skip the application


def add(n1,n2):
    print("addition is:",n1 + n2)

def squ(n1,n2):
    print("square is:",n1 **2)
    print("square is:",n2 **2)
    
def expo(n1,n2):
    print("addition is:",n1 ** n2)

# def cont():
#     if (input("Enter you want to continue or not(y/n)").lower() !='y'):
#         break

while (True):
    
    print("1.Addition\n"
        "2.Squaring\n"
        "3.exponenation")

    no1 = int(input("Enter first no: "))
    no2 = int(input("Enter Second no: "))
    task = str(input("enter the action: "))

    if task == "addition":
        callfun = add(no1,no2)

    elif task == "square":
        callfun = squ(no1,no2)
        
    elif task == "expo":
        callfun = expo(no1,no2)
        
    else:
        print("Wrong input")

    callfun = cont()

    if (input("Enter you want to continue or not(y/n)").lower() !='y'):
        break




















