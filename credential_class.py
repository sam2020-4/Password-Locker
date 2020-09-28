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

    