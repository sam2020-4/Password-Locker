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

