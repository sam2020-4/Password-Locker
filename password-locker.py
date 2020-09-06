#!/usr/bin/env python3.8
import random
from user import User
from user import Credential

def create_user(u_name,l_name,password):
    '''
    fuction to create new user
    '''
    new_user = User(u_name,l_name,password)
    return new_user

def create_credential(user_name, socialmedia, password):
    '''
    function to create new user account
    '''
    new_credential = Credential(user_name, socialmedia, password)
    return new_credential
