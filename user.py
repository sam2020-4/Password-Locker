import string
import secrets
import pyperclip

# user class starts here
class User:
    """
    class that generates new instances of user
    """

    user_list = [] #empty user list

    def __init__(self, u_name,l_name, password):
        
        self.u_name = u_name
        self.l_name = l_name
        self.password = password
    
    #save user
    def save_user(self):
        '''
        save_user method saves objects into user_list
        '''
        
        User.user_list.append(self)

    #displaying all saved users
    @classmethod
    def display_user(cls):
        '''
        this method returns user details.
        '''
        return cls.user_list    

    #deleting user
    def delete_user(self):
        '''
        function to delete user info
        '''
        User.user_list.remove(self)    
    

# class for Credential starts here
class Credential:
    '''
    this is the class to create account credentials, generate password and save the users information
    '''
    credential_list = []
    user_credentials_list = []

    @classmethod
    def check_user(cls,u_name,password):
        '''
        function that checks if the user name and password entered matches with the one on user_list.
        '''
        current_user = ""
        for user in User.user_list:
            if (user.u_name == u_name and user.password == password):
                current_user = user.u_name
                return current_user
    
    # declaring and initializing variables
    def __init__(self, user_name, socialmedia, password):
        '''
        method to define objects to be hold by the function
        '''
        self.user_name =user_name
        self.socialmedia = socialmedia
        self.password = password
    
    def save_credentials(self):
        Credential.credential_list.append(self)

    def delete_credentials(self):
        Credential.credential_list.remove(self) 

