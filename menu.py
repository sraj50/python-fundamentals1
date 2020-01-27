"""
Author: Siddharth Rajesh (23852860)
Start Date: 20th March 2019
Last Modified Date: 11th April 2019

Program Description:

This program is a menu that interacts with the user.

The main functions of the menu are to receive input values from the user, calculate the nerd score and determine
the nerd class.

The program validates the inputs before calculating the nerd score. Only integer values are allowed for input values.

When calculating the nerd score, the program also checks for any missing values and prompts the user accordingly.

After a nerd score is calculated only then a nerd class can be determined.

The user also has the option to terminate the program.
"""


# import library
import math

# import user defined module
from testInteger_23852860 import isInteger

nerdScoreList = []  # list to store the student's nerd score
nerdClassRating = []    # list to store the nerd ratings


# initialize input variables to NoneType i.e no value or absence of value
fandomScore = None    # store fandom score
hobbiesScore = None    # store hobbies score
sportsScore = None    # store sports score

# flag for while condition
flag = True

# while loop to continuously run until user exits program
while flag:

    # menu
    print(''' 
    1. Fandom
    2. Hobbies
    3. Sports
    4. Nerd Score
    5. Nerd Rating
    6. Exit
    \n
    ''')

    # prompt user to select option from menu
    option = input('Select an option: ')

    # validate for fandom score
    if option == '1':

        # prompt user for input
        fandomScore = input('Enter fandom score: ')

        # test input for integer, if pass do further validations
        if isInteger(fandomScore):

            # test for non-zero positive integer
            if int(fandomScore) < 1:

                # print error message
                print('INVALID! Please enter a non-zero positive integer')

                # reset variable to no value (NoneType) for invalid input
                fandomScore = None

            # print valid input
            else:
                print('Fandom score is %i!' % int(fandomScore))

        # input failed for integer test
        else:
            # print error message
            print('INVALID! Please enter only integer values')

            # reset variable to no value (NoneType) for invalid input
            fandomScore = None

    # validate for hobbies score
    elif option == '2':

        # prompt user for input
        hobbiesScore = input('Enter hobbies score: ')

        # test input for integer, if pass do further validations
        if isInteger(hobbiesScore):

            # test for positive integer
            if int(hobbiesScore) < 0:

                # print error message
                print('INVALID! Please enter a positive integer')

                # reassign variable to none for invalid input
                hobbiesScore = None

            # test for multiple of four
            elif int(hobbiesScore) % 4 != 0:

                # print error message
                print('INVALID!, Please enter a score which is a multiple of four')

                # reset variable to no value (NoneType) for invalid input
                hobbiesScore = None

            # print valid input
            else:
                print('Hobbies score is %i!' % int(hobbiesScore))

        # input failed for integer test
        else:
            # print error message
            print('INVALID! Please enter only integer values')

            # reset variable to no value (NoneType) for invalid input
            hobbiesScore = None

    # validate for sports score
    elif option == '3':

        # prompt user for input
        sportsScore = input('Enter number of sports played: ')

        # test input for integer, if pass do further validations
        if isInteger(sportsScore):

            # test for positive integer
            if int(sportsScore) < 0:

                # print error message
                print('INVALID! Please enter a positive integer')

                # reassign variable to none for invalid input
                sportsScore = None

            # print valid input
            else:
                print('Number of sport(s) played: %i' % int(sportsScore))

        # input failed for integer test
        else:
            # print error message
            print('INVALID Please enter integers only')

            # reassign variable to none for invalid input
            sportsScore = None

    # calculate nerd score
    elif option == '4':
        print('Calculating nerd score...')

        # test for invalid or missing input values
        if fandomScore is None or hobbiesScore is None or sportsScore is None:

            # print error message
            print('ERROR!, One or more values are null!\n')

            # prompt user for missing values
            if fandomScore is None:
                print('\tERROR!, Fandom score value is null! Please go back and enter a value...')

            if hobbiesScore is None:
                print('\tERROR!, Hobbies score value is null! Please go back and enter a value...')

            if sportsScore is None:
                print('\tERROR!, Sports score value is null! Please go back and enter a value...')

        # calculate nerd score for valid inputs
        else:
            # calculate nerd score
            nerdScore = int(fandomScore) * math.sqrt((42 * int(hobbiesScore) ** 2) / (int(sportsScore) + 1))

            # append nerd score to output list
            nerdScoreList.append(nerdScore)

            # prints the nerd score as list
            print('Nerd score is: ', nerdScoreList)

    # find nerd class
    elif option == '5':
        print('Printing nerd rating..')

        # test for empty input list
        if len(nerdScoreList) < 1:

            # print error message
            print("Please enter some values to calculate nerd score and add at least 1 item into the list")

        else:
            # initialize the output list with values zero
            nerdClassRating = [0] * 7

            # iterate each score in list
            for each in nerdScoreList:

                # increment count at index 0 (Nerdlite) if nerd score greater than or equal to 0 but less than 1
                if 0 <= each < 1:
                    nerdClassRating[0] += 1

                # increment count at index 1 (Nerdling) if nerd score greater than or equal to 1 but less than 10
                elif 1 <= each < 10:
                    nerdClassRating[1] += 1

                # increment count at index 2 (Nerdlinger) if nerd score greater than 10 or equal to but less than 100
                elif 10 <= each < 100:
                    nerdClassRating[2] += 1

                # increment count at index 3 (Nerd) if nerd score greater than 100 or equal to but less than 500
                elif 100 <= each < 500:
                    nerdClassRating[3] += 1

                # increment count at index 4 (Nerdington) if nerd score greater than 500 or equal to but less than 1000
                elif 500 <= each < 1000:
                    nerdClassRating[4] += 1

                # increment count at index 5 (Nerdrometa) if nerd score greater than 1000 or equal to but less than 2000
                elif 1000 <= each < 2000:
                    nerdClassRating[5] += 1

                # increment count at index 6 (Nerd Supreme) if nerd score greater than or equal to 2000
                elif each >= 2000:
                    nerdClassRating[6] += 1

        # print nerd class
        print('Nerd rating: ', nerdClassRating)

    # terminate program
    elif option == '6':

        # prompt user for input
        exitOption = input('Are you sure you want to quit (y/n): ')

        # exit while loop if yes
        if exitOption is 'y' or exitOption is 'Y' or exitOption is 'yes' or exitOption is 'Yes' or exitOption is 'YES':
            flag = False

    # if any other option, prompt user to enter a valid option
    else:
        print('Invalid option! Please try again')

