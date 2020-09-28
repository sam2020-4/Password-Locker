#!/usr/bin/env python3.8
import pyperclip  #importing pyperclip for copying to clipboard
from user_class import User  #imporing user class
from credential_class import Credential #importing credential class


def create_user(fname, lname, password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname, lname, password)
	return new_user


def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name, password):
	'''
	Function that verifies the existence of the user before creating credentials
	'''
	check_user = Credential.check_user(first_name, password)
	return check_user


def generate_password():
	'''
	Function to generate a password automatically
	'''
	password_gen = Credential.generate_password()
	return password_gen

def check_existing_site(site_name):
    '''
    Function that check if a credential exists with that site_name and return a Boolean
    '''
    return Credential.find_by_site_name(site_name)


def create_credential(username, site_name, account_name, password):
	'''
	Function to create a new credential
	'''
	new_credential = Credential(username, site_name, account_name, password)
	return new_credential


def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)
	
def del_credential(site_name):
    '''
    Function to delete a credential
    '''
    Credential.delete_credentials()

def display_credentials(username):
	'''
	Function to display saved credentials
	'''
	return Credential.display_credentials(username)

def find_credential(site_name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credential.find_by_site_name(site_name)

def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(site_name)


def main():
	print(' ')
	print('Hello! Welcome to Password Lock.')
	while True:
			print("-"*30)
			print('\n')

			print('Use these short codes: \n ca - Create an Account \n li - Login \n ex - Exit')
			print('\n')
			short_code = input('Enter a choice: ').lower().strip()
			if short_code == 'ex':
				break

			elif short_code == 'ca':
				print("-"*20)
				print('\n')
				print('Create a new account:')
				print('\n')

				first_name = input('Enter your first name - ').strip()
				last_name = input('Enter your last name - ').strip()
				password = input('Enter your password - ').strip()
				save_user(create_user(first_name, last_name, password))
				print(" ")
				print(
					f'New Account Created for: {first_name} {last_name} using password: {password}')
				print('\n')

			elif short_code == 'li':
				print("-"*20)
				print('\n')
				print('Enter your account details to login:')
				print('\n')

				username = input('Enter your first name - ').strip()
				password = str(input('Enter your password - '))
				user_exists = verify_user(username,password)
				if user_exists == username:
					print('\n')
					print(f'Welcome {username}. Please select a short code to continue.')
					print(' ')

					while True:
						print("-"*30)
						print('Our short codes: \n cc-Create a Credential \n sc-Show Credentials \n fc- Find a Credential  \n copy-Copy Password \n ex-Exit')
						print('\n')
						short_code = input('Enter a choice: ').lower().strip()
						print("-"*10)

						if short_code == 'ex':
							print(" ")
							print(f'Thank you for using Password Lock. Goodbye {username}')
							break

						elif short_code == 'cc':
							print('\n')
							print('Enter your new credentials:')
							print('\n')
							site_name = input('Enter the site name- ').strip()
							account_name = input('Enter your account name - ').strip()

							while True:
								print('\n')
								print("-"*20)
								print('Please select an option for creating a password: \n ep - enter your password \n gp - generate a password \n ex - exit')
								psw_choice = input('Enter an option: ').lower().strip()
								print("-"*10)

								if psw_choice == 'ep':
									print('\n')
									password = input('Enter your password: ').strip()
									break
								elif psw_choice == 'gp':
									password = generate_password()
									break
								elif psw_choice == 'ex':
									break
								else:
									print('Wrong option entered. Try again!')

							save_credential(create_credential(username,site_name,account_name,password))
							print('\n')
							print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
							print('\n')						
							     
						elif short_code == 'fc':
							print("Enter the site name you want to search for:")
       
							site_name = input()
							if check_existing_site(site_name):
									credential = find_credential(site_name)
									print(f"Here is the Credentials for {credential.site_name} ")
									print('\n')
									print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
									print('\n')
									print('-' * 20)
         
							else:
									print('\n')
									print("That credential does not exist")
       
						elif short_code == 'rc':
							print('\n')
							print("Enter the site name of the credentials you want to remove")
							print('\n')
       
							site_name = input('Enter the site name- ').strip()
							# del_credential(credential)

							if find_credential(site_name):
									credential = find_credential(site_name)
									credential.delete_credentials()									
									print("Here is a list of all deleted credentials")
									print('\n')


							else:
									print('\n')
									print("That credential does not exist")
									print('\n')

						elif short_code == 'sc':
							print('\n')
							if display_credentials(username):
								print('Here is a list of all your credentials')
								print("  ")
								for credential in display_credentials(username):
									print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
								print('\n')
							else:
								print('\n')
								print("You don't seem to have saved any credentials yet. enter cc to create one.")
								print('\n')

						elif short_code == 'copy':
							print(' ')
							site_name = input('Enter the site name for the credential password to copy: ')
							copy_credential(site_name)
							print('\n')
						else:
							print('Wrong option entered. Try again!')

				else:
					print(' ')
					print('Wrong details entered. Try again or Create an Account!')

			else:
				print("-"*20)
				print('\n')
				print('Wrong option entered. Try again!')

if __name__ == '__main__':
	main()