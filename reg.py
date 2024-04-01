import re
string0 = "abcdefghijklmnopqrstuvwxyz@gmail.com"
string1 = "abcdefghijklmnopqrstuvwxyz1234567890@gmail.com"
string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ@gmail.com"
string3 = "0123456789@gmail.com"
string4 = "HELLOHEL@gmail.com "
string5 = "hellohel@gmail.com"
string6 = "hello123@gmail.com"
string14 = "hello123h@gmail.com"
string7 = "123hello@gmail.com"
string8 = "__"
string9 = "......"
string10 = "**************"
string11 = "```````````````"
string12 = "!!!!!!!!!!!"
string13 = ""
string15 = "abcdef highkl@gmail.com"
string16 = "a430928409238409234@gmail.cma"
string17 = "3543543547"

my_list = [string0,string1,string2,string3,string4,string5,string6,string14,string7,string8,string9,string10,string11,string12,string13,string15,string16,string17]



for reg in my_list:
    # result = re.search("^[a-z]+[0-9][com]+$",reg)
    result = re.findall("@gmail[\.]+com",reg)
    # result = re.search("[com]$",reg)
    # if result is not None:    
    #     print(f"{reg}")
    
    if result != []:
        print(reg)

# another method: 

# pattern = '^\d+[_a-zA-Z]'  take patt in variable 

# for test_string in my_list:
#     result = re.search(pattern, test_string)    pass variable
#     if result :
#         print(f"{test_string}")



