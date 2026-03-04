# Progress Report GPA Calculator
This is a simple python script to show all the chapter members who are below the required GPA at the time of progress reports. I have written instructions on how to run the script for both technical and non technical users.

## Technical users
Using the script is quite simple. I have included a requirements.txt file to make the instilation process even more simple. Just download the gpa.py file and requirements.txt file. If these insturctions are over your head, proceed to the 'Non-Technical' users section.

        pip install requirements.txt
        python3 gpa.py path/to/excel_file

## Non-Technical
In order to take advantage of this script, you first must have python installed. If you do not have python installed, follow the instructions in this video https://youtu.be/e70ykVBazAg?si=v4sdIvccIlVNDF2G

The next step is to download 2 files: __requirements.txt__ and __gpa.py__. These can be downloaded from _this_ github page :D . Place these files in the same folder for ease of use later. You should also place the excel file that contains the progress report grades in this folder.

Now, open that folder you just created. In that folder:

Shift + Right Click

Choose “Open in Terminal”

This should bring up a black box where you can type into. Type the following:

        pip install requirements.txt

That command just downloaded the rest of code we need to run our script. Once that is completed, we can finnaly run the script. To do so, use this command:

        python3 gpa.py name_of_excel_file

YOU CANNOT JUST COPY AND PASTE THIS COMMAND! To make this work, you must replace "name_of_excel_file" with the name of your excel file. For example, if your excel file was called "grades.xlsx", your command would look like this:

        ptyon3 gpa.py grades.xlsx

It is also very important that all of these files are in the same folder that you "Opened in Terminal". If they are not, place them in the same folder and try again.

If you did everything right, there should be an output of names in the black box window. The script will report the following information:

- Brothers whose GPA is below 2.6 + number of hours reported
- Brothers who have 0 classes reported for Progess reports


