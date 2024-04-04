import datetime

class server_management():
    
    server_name = "CDAC"

    def __init__(self, os_t, u_name, i_date):
        self.os_type = os_t
        self.user_name = u_name
        self.issued_date = i_date

        if  self.os_type == "ubuntu" or self.os_type == "centos" :
            with ( open ( "os_detail.txt" , "a+" ) as file1 ):
                file1.write(self.os_type+ "\n" +self.server_name+ "\n" +str(self.issued_date))
            
        else:
            print("Connect with the IT Team")

        
    def read_servr_entries(self):
        with ( open ("os_detail.txt", "r+") as file2 ):
            print(file2.read()) 
        
    def show_detail(self):
        return self.os_type, self.server_name, self.issued_date


def main():
    ost = input("Enter OS Type : ")
    ous = input("Enter User Name : ")
    idate =  datetime.datetime.now()
    s1 = server_management(ost, ous, idate)

    a, b, c = s1.show_detail()
    
    print("Server name : ", s1.server_name)
    print("OS Type : ", a)
    print("User Name : ", b)
    print("Date : ", c)

    s1.read_servr_entries()

main()
