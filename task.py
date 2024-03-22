# we will take number from the user 
# if the number is divisible by 3 print Fizz    
# if the number is divisible by 5 print Buzz
# if the number is divisible by 3 and also divisible by 5 print Fizz Buzz

no = int(input("Enter no :"))
result = no % 3
result1 = no % 5

if (result1 == 0 and result == 0):
    print("Fizz and Buzz")

elif (result == 0):
    print("fizz")

elif (result1 == 0):
    print("Buzz")

    
else:
    print("NOt found")
    
