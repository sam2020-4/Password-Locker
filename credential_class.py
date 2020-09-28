import pyperclip #importing pyperclip for copying to clipboard
import time,sys
from user_class import User #importing user class 
import random #import random variable generator
import string  #import string constants


class Credential:
	'''
	Class to create  account credentials, generate new passwords and save user information
	'''

	credentials_list =[]
	user_credentials_list = []

    def __init__(self,username,site_name,account_name,password):
		'''
		Method to define the properties for each user object.
		'''

		self.username = username
		self.site_name = site_name
		self.account_name = account_name
		self.password = password
    
    @classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered exist in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

    def save_credentials(self):
		'''
		Function to save a newly created user credentials
		'''

		Credential.credentials_list.append(self)
    
    @classmethod
	def delete_credentials(self):
		'''
		Function to save a newly created user credentials
		'''
				
		Credential.credentials_list.remove(self)
  


