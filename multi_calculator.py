#!/usr/bin/env python3
# Created by: Joseph Kwon
# Created on: Dec 07, 2022
# This program asks the user for the radius and height of a cylinder and outputs volume
# Additionally, it has a first letter capitalization program

# Input in main, output/return in function,

import math
import pyperclip

# The function below does not work for codespaces, requires pip install pyperclip

# def uppercaseSentence(sentence):

# upperSentencelist = list(sentence.lower())

# for i in range(len(sentence)):
# if i == 0:
# upperSentencelist[i] = sentence[i].upper()
# elif sentence[i - 1] == ' ':
# upperSentencelist[i] = sentence[i].upper()

# listToStr = ''.join([str(elem) for elem in upperSentencelist])

# return listToStr


def cylinder_calculator(radius, height):

    # process for volume
    volume = math.pi * pow(radius, 2) * height

    # output for the calculated answer (volume) find the return for this
    print("")
    print("\33[32mThe volume of the cylinder is = {:,.2f}".format(volume))


def circumfrence_calculator(
    radius,
    circle_name=None,
):

    # Calculating circumfrence
    circumfrence = 2 * math.pi * radius

    # Piecing together the info
    circumfrence_with_name = (
        "The circumfrence of the circle is "
        "{}"
        " and your circle's name is "
        "{}".format(circumfrence, circle_name)
    )

    # Default (name) is optional, hence in case default value.
    if circle_name != None:
        return circumfrence_with_name
    elif circle_name == None:
        return circumfrence


def main():

    try:
        # Convert the number to a float
        radius_from_user = float(input("Enter the radius (decimals): "))
    except:
        # In case of a invalid number inputted
        print("Invalid numbers. Please enter proper numbers.")
        # input("Enter any key to restart: ")
        main()
    try:
        height_from_user = float(input("Enter the height (decimals): "))
    except:
        # In case of a invalid number inputted
        print("Invalid numbers. Please enter proper numbers.")
        # input("Enter any key to restart: ")
        main()

    # Check if the user's input is negative
    if radius_from_user and height_from_user <= 0:
        print("Enter positive numbers")

    # If not, proceed to the function
    else:
        cylinder_calculator(radius_from_user, height_from_user)

    print("Second calculation, circumfrence of a circle:")
    try:
        radius_circle = float(input("What is the radius of your circle (decimals): "))
    except:
        # In case of a invalid number inputted
        print("Invalid numbers. Please enter proper numbers.")

    # Check if the user input is negative
    if radius_circle <= 0:
        print("Enter positive numbers")

    else:
        # Ask for the default value (name of the circle)
        user_circle_name = input(
            "Enter your circle's name if it has one. (Press enter to skip this): "
        )

        # Checks if the user entered a name. If they did, the circle's name
        # is passed to the function
        if user_circle_name != "":
            circumfrence_calculation = circumfrence_calculator(
                radius_circle, user_circle_name
            )

        # If the user did not enter a name, only the radius is passed to the function
        else:
            circumfrence_calculation = circumfrence_calculator(radius_circle)

        # Get the finished calculated result from the circumfrence calculator function
        print("")
        print(circumfrence_calculation)

        # The body paragraph has been commented out because it does not work for codespaces

        # user_answer = input("Would you like to try a third problem? Y|N (does not work for codespaces")
        # if user_answer = "Y" or "y":
        # userSentence = input("Enter a sentence: ")
        # pyperclip.copy(uppercaseSentence(userSentence))
        # print("Copied to clipboard!")
        # input("Enter anything to exit: ")
        # else:
        # print("Third problem will not be completed")


if __name__ == "__main__":
    main()
    # ask the user for "y" or "n" to continue
    answer = input("Would you like to try again? (y/n): ")
    # use a while loop to loop back if user's input is "y"
    while answer == "y":
        main()
        answer = input("Would you like to try again? (y/n): ")

    # if user inputs n, thank them for playing
    if answer == "n":
        print("Thank you for playing.")

    # else, if none of the options above were inputted, output default message
    else:
        print("Program has ended.")
