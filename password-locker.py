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


def save_user(user):
    '''
    function to save user
    '''
    user.save_user()

def save_credentials(credential):
    '''
    function to save a new user credential
    '''
    Credential.save_credentials(credential)

def varify_user(user_name, password):
    '''
    Function to varify the existence of the user
    '''
    checking_user = Credential.check_user(user_name,password)
    return checking_user

def delete_user(user):
    '''
    function to delete a user
    '''
    user.delete_user()

def display_user():
    '''
    function that returns all the saved users
    '''
    return User.display_user()

def generate_password(pass_len):
    '''
    a function that generates password automatic
    '''
    return Credential.generate_password(pass_len)

@classmethod
def find_by_socialmedia(cls, socialmedia):
    '''
    a function to seqrchfor the saves credentials
    '''
    return cls.find_by_socialmedia(cls, socialmedia)

@classmethod
def copy_credentials(cls, socialmedia):
    '''
    a class method to enable use to copy credentials to the clipboard
    '''
    return cls.copy_credentials(cls, socialmedia)
