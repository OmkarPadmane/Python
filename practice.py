# 1) Get the height from the user in cms and display the user height back to console
# in foot/feet and inches

# def height(h1):
#     print("Height in feet is " , round((h1/30.48),2))


# height1 = int(input("Pleased enter height in cms :"))
# callfun = height(height1)


# 2) Get the no of the dollars from the user apply the conversion of 
# 1 dollar = 82 rupees and print the amount to the console in rupees

# def conversion(money):
#     # ind = rup * 82
#     print("Doller" , money , "in rupees are : ", money  * 82)
    
# dol = int(input("enter Doller :"))    
# callfun = conversion(dol)


# def my_addition_function(num1,num2):
#     return num1+num2

# my_first_number = 1
# my_second_number = 2 

# return_val = my_addition_function(my_first_number,my_second_number)
# print("Returned value from my_addition_function is ", return_val)



def sub(no1,no2):
    return no1 - no2 

no1 = int(input("first no:"))
no2 = int(input("second no:"))

return_val = sub(no1,no2)
print("returned value from sub is ",return_val)

