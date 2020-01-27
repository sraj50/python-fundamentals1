"""
Author: Siddharth Rajesh (23852860)
Start Date: 20th March 2019
Last Modified Date: 11th April 2019

Program Description:

    calculateSkillEquation(x, y, z)

    Function Summary:
        Calculates the nerd score based on the formula and appends nerd score to a list.
        Tests the input parameters for integer values and if passed further validations for range of allowed values

    Parameters:
        x(int): fandom score
        y(int): hobbies score
        z(int): sports score

    returns:
        outputList(list): the nerd score calculated is appended to a list
        None(NoneType): for invalid input parameters
"""

# import math library
import math


# global variable list to store nerd score
outputList = []  # initialize the output list

# global variable for validation
flag = True


# x, y, z are inputs
def calculateSkillEquation(x, y, z):

    # define as global as flag value will change based on condition
    global flag

    # comparing type of each input, if input is anything other than integer, throw error
    if type(x) is not int or type(y) is not int or type(z) is not int:

        print('ERROR! One or more inputs received are not integers, please provide only integer values!')

        if type(x) is not int:
            print('x is not an integer, please provide an integer value to x')

        if type(y) is not int:
            print('y is not an integer, please provide an integer value to y')

        if type(z) is not int:
            print('z is not an integer, please provide an integer value to z')

        flag = False

    # else calculate nerd score for inputs of integer types
    else:

        # test for range on x
        # test for non-zero positive integer
        if int(x) < 1:
            # print error message
            print('INVALID! Please enter a non-zero positive integer for x')
            flag = False

        # test for range on y
        # test for positive integer
        if int(y) < 0:

            # print error message
            print('INVALID! Please enter a positive integer for y')
            flag = False

        # test for multiple of four
        if int(y) % 4 != 0:

            # print error message
            print('INVALID!, Please enter a score which is a multiple of four for y')
            flag = False

        # test for range on z
        # test for positive integer
        if int(z) < 0:
            # print error message
            print('INVALID! Please enter a positive integer z')
            flag = False

        # return none for invalid inputs
        if flag is False:
            return None

        # return nerd score
        else:

            # calculate nerd score
            skillScore = x * math.sqrt((42 * y ** 2) / (z + 1))

            # append nerd score to output list
            outputList.append(skillScore)

            # return output nerd score list
            return outputList


# run main function
if __name__ == '__main__':

    # input parameters to calculate nerd score
    fandomScore, hobbiesScore, sportsNum = 1, 4, 1

    # print nerd score value as list
    print('Nerd Score: ', calculateSkillEquation(fandomScore, hobbiesScore, sportsNum))
