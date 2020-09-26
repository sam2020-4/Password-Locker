#!/usr/bin/env python3.8
import pyperclip
from user import User
from user import Credential

def create_user(first_name, last_name, email, phone_number, password):
    '''
    Function to create a new user account
    '''
    new_user = User(first_name, last_name, email, phone_number, password)
    return new_user

def create_credential(user_name, site_name, account_name, password):
    '''
    Function to create a new user account
    '''
    new_credential = Credential(user_name, site_name, account_name, password)
    return new_credential

def save_user(user):
    '''
    Function to save a new user account
    '''
    User.save_user(user)

def save_credentials(credential):
    '''
    Function to save a new user account
    '''
    Credential.save_credentials(credential)

def verify_user(first_name, password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = Credential.check_user(first_name, password)
    return checking_user

def generate_password(pass_len):
    '''
    A funtion to generate password, combining random letters and digits
    '''
    return Credential.generate_password(pass_len)


    


if __name__ == '__main__':
    main()