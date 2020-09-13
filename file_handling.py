import os
import xlsxwriter
Alphabet = ["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","K1","L1","M1","N1","O1","P1","Q1","R1","S1","T1","U1","V1","W1","X1"]
def count_files(dire):
    global directory
    directory= {}
    current_dir = ""
    try:
        current_dir = os.chdir(dire)
    except:
        return False
    diretories = os.listdir()
    
    x = 1
    for dir in diretories:
        if os.path.isfile(dir):
            extension = os.path.splitext(dir)[1]
            if extension == "":
                extension = os.path.splitext(dir)[0]
            if extension in directory.keys():
                directory[extension] +=1
                x+=1
            else:
                directory[extension] = 1
                x+=1
    return directory

def list_all_files_according_to_extension(dir):
    directory = {}
    for dirName,dirList,fileList in os.walk(dir):
        files = {}
        files = count_files(dirName)
        directory[dirName] = files
    return directory


def look_for_specific_extenion(dir,extension):
    x = 0
    files = {}
    files = list_all_files_according_to_extension(dir)
    for v in files.values():
        if extension in v.keys():
            x += v[extension]
    return {extension:x}

def write_in_excel(result):
    os.chdir("/home/ubuntu/Desktop")
    #merging all the extensions in one dictionary without duplication
    file_types = list(result.values())
    unique_files = {}
    for f in file_types:
        unique_files.update(f)
    #adding headers based on extensions
    columns = list(unique_files.keys())
    workbook = xlsxwriter.Workbook("report.xlsx")
    worksheet= workbook.add_worksheet()
    bold = workbook.add_format({"bold":True})
    global Alphabet
    worksheet.write(Alphabet[0],"directory",bold)
    for i,v in enumerate(columns):
        worksheet.write(Alphabet[i+1],v,bold)
    #adding values for each column
    row =1
    for k,v in result.items():
        worksheet.write(row,0,k)
        for k1,v1 in v.items():
            worksheet.write(row,columns.index(k1)+1,v1)
        row +=1
    workbook.close()
    os.chdir("/home/ubuntu")
print("\n")
print("Hello this is a python program which count all the files and group them by theirs extension:_",end="_")
input()
print("You can Enter the directory and then get all the files:",end="_")
input()
def validate_input(dir_name):
    try:
        os.chdir(dir_name)
        return True
    except:
        return False
directory = input("Please Enter the Directory name:_   ")
while not(validate_input(directory)):
    directory = input("Please Enter a valid directory:_   ")

result = list_all_files_according_to_extension(directory)
print("\n")
print("here you go !")
print("\n")
print("==========================================Result============================================")
print("\n")
for k,v in result.items():
    print(k+":")
    for k1,v1 in v.items():
        print("\t"+k1+": "+str(v1))
print("\n")
print("==========================================Result============================================")
print("\n")
print_report = input("You want to write it in excel file?(y/n)  ")
print("\n")
if print_report == 'y' or print_report == 'Y':
    write_in_excel(result)
    print("successfuly wrote")
    print("\n")
print("bye have a good day")


