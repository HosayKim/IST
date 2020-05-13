# Password is "1359"

# Imports the main_menu function from the MainMenu file
from MainMenu import main_menu

# Prints titles of program followed by a blank line
print("Gowan Brae Public School - Test Scores Program")
print()


# Logs the user in
def login(attempts=1):
    # Gets the user's input
    pin = input("Please enter your pin? ")

    # Checks if the users input equals to the correct pin
    if pin == "1359":
        print("Login Successful")
        # Sends the user to the main menu
        main_menu()
    # Gives the user another attempt
    elif attempts < 3:
        print("Please try again.")
        login(attempts=attempts + 1)
    # Closes the program because there have been too many attempts
    else:
        print("Too Many Attempts")
        exit()


# Starts the login function
login()
