# Count and Categorize files
The 'count and categorize files' app is a simple console app written in python programming lauguage that can be used very easily.
The app provides a report that shows how many files from each type of file you have. 
## Features
- This app get the name of directory from the user, user can enter any directory he/she wants.
- app validate the input of user does it exist in directories or no if yes it will be   continued otherwise app request for another input.
- app walk through all the sub directories and find the files and categorize them.at end export the result as a excel file, which is so easy to undrestand.
- app will continue to its process, untill the user doesn't terminat the app.
- user can terminate the app anytime by entering 0.
## Getting started
Prerequisites:
- python interpreter must be installed in your computer
- import os module for directory handling
- install and import XlsxWriter package for adding and edit xlsx files.
Running App:
- open your terminal and run the following command
- Get the code:
    ```
    git clone https://github.com/AbCreativeAmid/count_and_categorize_files.git
    ```

- then enter to folder and run __init__.py file
- At first the app shows a brief description of app it shows app is insalled and working successfuly
  is installed
## How Does It Work?
- This app consist three modules file_handling.py write_in_excel.py and __init__.py
- In file handling module the input will be validated and all the files will be fetched and categorized.
- In write_in_excel module the result of file_handling module will be written in excel file
- In __init__ module, it is for intracting with user get the user input and uses two other modules for completing the tast and shows the out to the user.
- when you run the app after the brief description-->
- app ask for directory name 
- then app asks for generating excel report and the name of report( you can enter the name of report )
- then app asks for another directory
- you can repeat for all directory you want 
- at end app will show you a good bye message it means all the prcess is done successfuly 
## Contributing
- for any suggestion and problem in this program you can share your idea through this email hussainiabdullah786@gmail.com
### Generating Excel File
-in this app a class created for generating excel report. by using this class generating excel file will be so so easy.
## License
Copyright (c) AbCreativeAmid. All rights reserved.
