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




if __name__ == '__main__':
    main()