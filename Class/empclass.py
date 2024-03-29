#  Exercise 01 : Classes and objects -- try creating this in oops world
# -------------------------------------------
# Employee
#   # instance variables 
#    emp_id
#    emp_salary
#    mgr_id
#   # class variable 
#   department_name
  
#   # instance methods
#   get_emp_salary()-> emp_salary
#   set_emp_salary(rcv_salary)-> emp_salary

#   # class method 
#   get_department_name() --> department_name
  
#   # static method
#   field_expertise() --> just displays some expertise for all my employees
  
# main:
# 1) create an object employee(100,1000,1)  
# 2) do the following for the created object
# // direct access using .notation
# empid
# emp_salary
# mgr_id
# 3) print the department name 
# 4) display the expertise for the employees 
# 5) Deleting Attributes and Objects


class Employee:
    department_name = "IT"
    
    @classmethod
    def __init__(self,id ,sal,manager):
        self.emp_id = id
        self.emp_salary = sal
        self.mgr_id = manager
        
    def get_emp_salary(self):
        return self.emp_salary    
    
    
    def set_emp_salary(self,rcv_salary):
        self.emp_salary = rcv_salary 
        
    def get_department_name(self):
        return self.department_name

    @staticmethod
    def field_expertise():
        print(" ---SKILLS ")
        
        
        
        
        
        
#########################################       
def main():
    emp1=Employee(100,1000,1)
    print("ID : ",emp1.emp_id)
    print("SALARY : ",emp1.emp_salary)
    print("MANAGER ID : ",emp1.mgr_id)
    print("DEPARTMENT : ",emp1.get_department_name())
    emp1.set_emp_salary(5000000000)
    print(emp1.get_emp_salary())
    emp1.field_expertise()
    del emp1.emp_salary
    print(emp1.emp_salary)
    
    del emp1
 
main()

















































