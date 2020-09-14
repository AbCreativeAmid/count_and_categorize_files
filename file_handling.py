import os
def validate_input(diretory_name):
    try:
        os.chdir(diretory_name)
        return True
    except:
        return False

def categorize_files_extension(dir_name):
	""" get directory name as parameter. this function categorize all existing files
	    according to their extension """
    extesion_files = {}
    current_dir = os.getcwd()
    os.chdir(dir_name)
    files = os.listdir()
    count = 1
    for f in files:
        if os.path.isfile(f):
            file_name = os.path.splitext(f)
            extension = file_name[1] if file_name[1]!="" else file_name[0]
            if extension in extesion_files.keys():
                extesion_files[extension] += 1
            else:
                extesion_files[extension] = 1
    os.chdir(current_dir)
    return extesion_files

def get_files(dire_name):
	"""this function take directory name as parameter and return a dictionary which 		   contain all the subdirectories with thier files and files are cotegorized      		   according  to their extension by calling other function"""
    files = {}
    for dir_name,dir_list,file_list in os.walk(dire_name):
        files[dir_name] = categorize_files_extension(dir_name)
    return files
def file_types(result_dictionary):
	"""this function take a dictionary as parameter and result the unique list of existing 		   extensions """
    extensions = {}
    for k1,v1 in result_dictionary.items():
        extensions.update(result_dictionary[k1])
    return list(extensions.keys())
