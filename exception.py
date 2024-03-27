is_not_correct_a = True
while(is_not_correct_a):
    try:
        a = int(input("enter the number a: "))
        is_not_correct_a = False
    except: 
        print("its incorrect number, please enter the correct value a : ")

is_not_correct_b = True
while(is_not_correct_b):
    try:
        b = int(input("enter the number b: "))
        is_not_correct_b = False
    except: 
        print("its incorrect number, please enter the correct value b : ")


c=(a + b)
print("the result of adding is: ",c)