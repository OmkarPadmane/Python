def list_display_members(members) :
	print(members)

def list_add_element(members) :
    list_display_members(members)
    members.append(input("Enter a new member: "))
    list_display_members(members)
    
def list_add_elements(members):
    list_display_members(members)
    members.extend((input("Enter members: ").split(',')))
    list_display_members(members)

def list_remove_element(members) :
    list_display_members(members)
    members.remove(input("Enter element to remove: "))
    list_display_members(members)

def remove_last_element(members) :
    list_display_members(members)
    members.pop()
    list_display_members(members)
    
def display_3_4_5_element(members):
    list_display_members(members)
    print(members[2:5])
    list_display_members(members)
    
			
def my_list_store():
    print("\n Welcome to Our List Store !!! ")
    print("Please enter a list Comma seperated that you would want to perform Operation Upon")
    members = input('Enter a list :\n').split(',')

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display all elements in the members list")
        print("  2:  Add an element to the members collection like 'Sehwag' ")
        print("  3:  Add elements to the members collection like ['David','Bret','Sanju']")
        print("  4:  Remove a member from the collection at a given subscript")
        print("  5:  Remove the last member from the collection ")
        print("  6:  Display third, fourth and fifth element from the collection ")
        print("  7: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            list_display_members(members) 
        elif choice ==2:
            list_add_element(members) 
        elif choice ==3:
            list_add_elements(members)
        elif choice ==4:
            list_remove_element(members) 
        elif choice ==5:
            remove_last_element(members) 
        elif choice ==6:
            display_3_4_5_element(members) 
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_list_store()		
