# -------------------------------------------
# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 
import random
from empclass import Employee

class Airlines(Employee):
    
    Airline = "Podaaa"
        
    def __init__(self):
        self.depature=""
        self.arrival=""
        self.flight=""
        self.seat =""
    
    def setter(self,depr,arr):
        self.depature = depr
        self.arrival = arr
        
        
    def get_values(self):  
        return self.depature, self.arrival, self.flight, self.seat 
        
    def seat_assign(self):
        n=random.randrange(1,40)
        a=random.choice(['A','B','C','D','E','F'])
        
        self.seat =str(n)+a
    
    def flight_no(self):
        self.flight = random.randrange(10000,99999)
        
        
        
def main():
    ticket=Airlines()
    d=input("ENTER THE DEPARTURE CITY : ")
    a=input("ENTER THE ARRIVAL CITY : ")
    ticket.setter(d,a)
    ticket.flight_no()
    ticket.seat_assign()     
    ticket.book_tik()
     
    
    
    
    print("\t\t\t\t",ticket.Airline,"\n ############################################################################# \n \t\t\t TICKET ")
    a,b,c,d = ticket.get_values()
    print("\t* DEPARTURE : ",a ,"\t\t\t","* ARRIVAL : ",b,"\t")
    print("\n \t* FLIGHT NO : ",c,"\t\t\t","* SEAT NO : ",d,"\t","\n #############################################################################")

main()
    


        
        
        
        
        
        
        
        