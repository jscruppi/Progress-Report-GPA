"""

Calculator for GPA's based on progress report .xlsx file

Authors: Joe Scruppi
Last Updated: 3.4.26

"""

import sys
import os
import csv
import pandas as pd

def calcCredits(letter_grade, course_num):
    
    factor = calcHours(course_num)

    match letter_grade[0]:
        case 'A':
            return 4 * factor
        case 'B':
            return 3 * factor
        case 'C':
            return 2 * factor
        case 'D':
            return 1 * factor
        case 'F':
            return 0 * factor
        case _:
            print(f'({letter_grade}) did not match')
            return

def calcGPA(credits, classes):
    if(credits == 0):
        return 0
    else:
        return float(credits) / float(classes)
        
def calcHours(course_num):

    #have to do this in case anyone has a 3 digit class number
    try:
        hours = int(course_num[3])
    except:
        hours = int(course_num[2])
    return hours

def main():
    #convert excel file to csv
    file = sys.argv[1]

    df = pd.read_excel(file, sheet_name=0)
    #save to csv
    df.to_csv('output.csv', index=False)

    curr_name = ''
    num_hours = 0
    total_credits = 0


    with open('output.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        for row in reader:
            if(curr_name != row['First Name'] + ' ' + row['Last Name']):

                if(num_hours != 0 and calcGPA(total_credits, num_hours) < 2.6):
                    print(f'{curr_name} GPA:')
                    print(f'{calcGPA(total_credits, num_hours):.2f} || {num_hours} credit hours\n')
                if(num_hours == 0 and curr_name != ''): 
                    print(f'{curr_name} has no reported grades!\n')
                num_hours = 0
                total_credits = 0
                curr_name = row['First Name'] + ' ' + row['Last Name']

            #there is a progress grade
            if(row['Progress Grade'] != ''):
                num_hours += calcHours(row['Course#']) 
                total_credits += calcCredits(row['Progress Grade'], row['Course#'])

    os.remove('output.csv') #the .xlsx to .csv file, dont need it anymore


if __name__ == '__main__':
    main()

