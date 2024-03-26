# Operations supported by our program are :
#     1: Display number of elements in the capitals collection
#     2: Add an element to the capitals collection like --> Afghanistan: Kabul
#     3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella
#     4: Remove an element from the collection 	
#     5: Take a key from the user and show value if it is present in the dictionary
#     6: Take a key from the user update it if it is present in the dictionary or add the key to the dictionary 	




# Sample code template for my_dict_store
def dict_display_capitals(capitals): 
    print(capitals)
    

     
def dict_add_element(capitals):
    key = input("enter the country")
    value = input("enter the capital")
    capitals.update({key : value})   
    print(capitals)
   
        
def dict_add_elements(capitals):
    for i in range( 0 ,  int(input("enter how many collection you want to add : "))):
        key=input("enter the country :")
        value=input("enter the capital :")
        capitals.update({key  : value})   
    print(capitals)
    
        
def dict_remove_element(capitals):
    key =input("enter the country :")
    del capitals[key]
    print(capitals)
    # print("Unimplemented , Write your code here") 

def dict_show_value_for_a_key(capitals):
    key =input("enter the country :")
    print("capital of " ,key , " : " ,capitals.get(key))
    
    # print("Unimplemented , Write your code here") 

def dict_update_or_add_a_key(capitals):
    key =input("enter the country :")
    value=input("enter the capital :")
    capitals.update({key : value})
    print(capitals)
    # print("Unimplemented , Write your code here") 

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
	
    capitals= {}

    
    for i in range( 0 ,  int(input("enter how many collection you want to add : "))):
        key=input("enter the country :")
        value=input("enter the capital :")
        capitals[key] = value
    
    
    # print("Unimplemented , Write your code here to create the dictionary from the user and reference it with capitals") 
    print(capitals)
    
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display all elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: get value for key 	")
        print("    6: asal tar update kar nasal tar add kar	")
        print("    7: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_element(capitals)
        elif choice ==3:
            dict_add_elements(capitals)
        elif choice ==4:
            dict_remove_element(capitals) 
        elif choice ==5:
            dict_show_value_for_a_key(capitals)
        elif choice ==6:
            dict_update_or_add_a_key(capitals)
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_dict_store()