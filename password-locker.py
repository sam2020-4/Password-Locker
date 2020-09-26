#!/usr/bin/env python3.8
# import random
# from user import User
# from user import Credential

# def create_user(first_name,last_name,email,phone_number,password):
#     '''
#     fuction to create new user
#     '''
#     new_user = User(first_name,last_name,email,phone_number,password)
#     return new_user

# def create_credential(user_name, socialmedia, password):
#     '''
#     function to create new user account
#     '''
#     new_credential = Credential(user_name, socialmedia, password)
#     return new_credential


# def save_user(user):
#     '''
#     function to save user
#     '''
#     user.save_user()

# def save_credentials(credential):
#     '''
#     function to save a new user credential
#     '''
#     Credential.save_credentials(credential)

# def varify_user(user_name, password):
#     '''
#     Function to varify the existence of the user
#     '''
#     checking_user = Credential.check_user(user_name,password)
#     return checking_user

# def delete_user(user):
#     '''
#     function to delete a user
#     '''
#     user.delete_user()

# def display_user():
#     '''
#     function that returns all the saved users
#     '''
#     return User.display_user()

# def generate_password(pass_len):
#     '''
#     a function that generates password automatic
#     '''
#     return Credential.generate_password(pass_len)

# @classmethod
# def find_by_socialmedia(cls, socialmedia):
#     '''
#     a function to seqrchfor the saves credentials
#     '''
#     return cls.find_by_socialmedia(cls, socialmedia)

# @classmethod
# def copy_credentials(cls, socialmedia):
#     '''
#     a class method to enable use to copy credentials to the clipboard
#     '''
#     return cls.copy_credentials(cls, socialmedia)

# def main():
#     print("Hello, Welcome to the Password Locker App!!, please Enter your name?")
    
#     user_name = input()
#     print(f"woow!!! welcome back {user_name}.\n; Enter other Name")
    
#     user_name = input()
#     print('\n')  

#     while True:
#         print('\n')
#         print("use these short codes: ca - creates a new user, \n du - display users, \n fc -find a user, \n ex -exit the user list ")
#         print('\n')

#         short_code = input().lower()

#         if short_code == "ca":
#             print("new_user")
#             print("_"*10)

#             print("Enter user name...")
#             user_name = input()           
            
#             print("Do you want to input your own password or have one generated for you? use short codes\n'gp\n' to generate password.\n \'cyo\' to choose your own password \n \'ex\' to exit...")
#             password_choice = input()
#             password = ''

#             if password_choice == "cyo":
#                 password = password.join(input("Enter a password of choice........"))
#                 # break
            
#             elif password_choice =="gp":
#                 print("enter the lenght of password")
#                 pass_len = input()
#                 password = password.join(Credential.generate_password(pass_len))
#                 # break

#             elif password_choice == 'ex':
#                  print('bye no password found!!!.......')
#                  break                
            

#             elif short_code == 'ex':
#                 print('bye!!!.......')
#                 break
            
#             else:
#                 print('sorry, i did not get that......please try again!!')

#             if short_code == 'cc':
#                 print('\n')
#                 print("Enter your credential details")
               
#                 print(f"Enter username ")
#                 user_name = input()
#                 print(f"Enter socialmedia")
#                 socialmedia = input()

#                 print(f"Enter the username you used or would love to use on {socialmedia}")
#                 user_name = input()
            
#             else:
#                 print("wrong credentials entered")

# if __name__ == '__main__':
#     main()