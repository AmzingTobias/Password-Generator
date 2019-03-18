import random #Importing the random module
import string #Importing the string module

def validateNumber():
    while True:
        try:
            passwordLength = int(input("How long do you want the password to be? "))  # Asking for user input on how long to make the password
            break #breaks the while loop
        except ValueError: #Incase the code above produces a value error
            print("Enter a number")
    return passwordLength #Returns the variable to

alphabet = list(string.ascii_lowercase) #Used to store a lower case alphabet as a list
alphabetUpper = list(string.ascii_uppercase) #Used to store an upper case alphabet as a list
alphabetSpecial = ["@","/",">","<","£","%","$","&","*","!","?"] #A list full of special cases

passwordLength = validateNumber() #Used to validate to make sure the user enters a correct number

passwordList = [None] * passwordLength #Creates a list with the length supplied by the user
for i in range(0,passwordLength): #Runs a for loop for x amount of times as the length of the list
    choice = random.randint(1,3) #Selects 1 of 3 alphabets to pick from
    if choice == 1:
        character = alphabet[random.randint(0, 25)] #Picks a random character from that list
    elif choice == 2:
        character = alphabetUpper[random.randint(0, 25)]
    else:
        character = alphabetSpecial[random.randint(0, 10)]
    passwordList[i] = character #Sets the value of data in the list at that location to the random character

password = "".join(passwordList)
print("Password: " + password)
#Joins the list together with no spacing to create the password
input()