"""
Author: Siddharth Rajesh (23852860)
Start Date: 20th March 2019
Last Modified Date: 11th April 2019

Program Description:

    countStudentClass(nerdScoreList)

    Function Summary:
        Determines the nerd class based on the nerd score and counts the occurrences of nerd scores belonging to
        each nerd class based on the input list of nerd scores.

    Input Parameters:
        nerdScoreList(list): list of nerd scores

    Returns:
        nerdCountList(list): list of counts for each nerd class in corresponding index
"""


def countStudentClass(nerdScoreList):

    # check for input list is empty
    if len(nerdScoreList) < 1:

        # print error message
        print("Please enter some values to calculate nerd score and add at least 1 item into the list")

        # return none
        return None

    else:
        # initialize the output list with values zero
        nerdCountList = [0] * 7

        # iterate each score in list
        for each in nerdScoreList:

            # increment count at index 0 (Nerdlite) if nerd score greater than or equal to 0 but less than 1
            if 0 <= each < 1:
                nerdCountList[0] += 1

            # increment count at index 1 (Nerdling) if nerd score greater than or equal to 1 but less than 10
            elif 1 <= each < 10:
                nerdCountList[1] += 1

            # increment count at index 2 (Nerdlinger) if nerd score greater than 10 or equal to but less than 100
            elif 10 <= each < 100:
                nerdCountList[2] += 1

            # increment count at index 3 (Nerd) if nerd score greater than 100 or equal to but less than 500
            elif 100 <= each < 500:
                nerdCountList[3] += 1

            # increment count at index 4 (Nerdington) if nerd score greater than 500 or equal to but less than 1000
            elif 500 <= each < 1000:
                nerdCountList[4] += 1

            # increment count at index 5 (Nerdrometa) if nerd score greater than 1000 or equal to but less than 2000
            elif 1000 <= each < 2000:
                nerdCountList[5] += 1

            # increment count at index 6 (Nerd Supreme) if nerd score greater than or equal to 2000
            elif each >= 2000:
                nerdCountList[6] += 1

        return nerdCountList    # return nerd class list


# run main function
if __name__ == '__main__':

    # input nerd score list
    studentScoreList = [23, 76, 1300, 600]

    # print nerd class rating
    print('Nerd Rating: ', countStudentClass(studentScoreList))
