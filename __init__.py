from file_handling import *
from write_in_excel import *

def print_result(result):
    print("======= Here you go! ==========")
    print("============== result ==================")
    for k,v in result.items():
        print(k)
        for k1,v1 in v.items():
            print("\t"+k1+":"+str(v1))
    print("============== end result =================")
def generat_excel_report(name,result):
    excel_rep = Excel_report(name)
    excel_rep.set_style("bold")
    excel_rep.set_headers(file_types(result))
    excel_rep.fill_data(result)
    excel_rep.close()
    print("report generated Successfully in "+str(os.getcwd())+" by "+name+".xlsx name")

input("Hello This is Count file program!_   ")
input("You can Enter the name of directory and the program give you back all files in directory and categrozie according to their extension:_")


while True:
    directory_name = input("Enter the name of directory please!_ or Enter 0 for exit:_  ")
  
    if validate_input(directory_name):
        result = get_files(directory_name)
        print_result(result)
        print_report = input("Do you want extract the result in excel file? if Yes Enter the filename either Enter 0!_   ")
        try:
            a = eval(print_report)
            break
        except:
            generat_excel_report(print_report,result)
           
    else:
        input("Oops! No such directory exist!_  ")
        input("Enter the name correctly and check speeling carefully!_ or Enter 0 for ending program!_  ")
        continue
    continue_pro = input("Do you want to try another directory? then Enter Y either any key for termination!_    ")
    if continue_pro == "y" or continue_pro == "Y":
        continue
    else:
        break
print("Bye! have a good day!")