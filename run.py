#!/usr/bin/env python3.6
from user import User
import getpass
import random
import string
dash = '-' * 60

def create_account(account_name,username,password,confirm_password):

    """
    function to create a new account
    """

    new_user = User(account_name,username,password,confirm_password)

    return new_user

def save_details(user):

    """
    function to save save_details
    """
    user.save_detail()

def display_all_details():

    """
    function used to return all saved save_details
    """
    return User.display_all_details()

def check_existing_user(username):

    """
    a function that is used to check and return all exissting accounts
    """

    return User.user_exist(username)

def find_user(username):

    """
    the function is used check details from the saved save_details
    """

    return User.find_by_username(username)

def generatePassword(num):
   genpas = ''

   for n in range(num):
       x = random.randint(0,94)
       genpas += string.printable[x]

   return genpas

def main():

print('\n')

    print('{:_^20}'.format('login'))

    print('\n')

    print("Please idetify yourself using your locker USERNAME")

    user_name = input().upper()

    print(f"Hello {user_name}, welcome to your password manager, how can we help you today")

    print('\n')

    while True:

        list =('''
        1-Register a new account
        2-Display accounts
        3-Find accounts
        4-Exit the locker\n''')
        print(list)
        short_code = input().lower()

        if short_code == '1':

            print(f"{user_name} Please FILL IN the following")

            print("-"*10)

            print ("Account name")

            account_name = input()

            print('\n')

            print("Username")
            username = input()

            print('\n')

            print("Do you want a randomly generated password?")


            print("yes", "no")
            ans = input().lower()

            if ans == 'yes':

                genpas = print(generatePassword(10))

                save_details(create_account(account_name,username,password,confirm_password))

                print ('\n')


                print(f"{user_name} {account_name} account of {username} created and password saved")

                print ('\n')


            elif ans == 'no':
                password = getpass.getpass('password:')
                print("*********")

                confirm_password = getpass.getpass('confirm password:')
                print("*********")

                save_details(create_account(account_name,username,password,confirm_password))

                print ('\n')

                print(dash)

                print(f"Hey {user_name}")
                print(f"Your account name is {account_name}.com")
                print(f"Your account username is {username}")
                print("passwords encripted but can be viwed using option 2 / 3")
