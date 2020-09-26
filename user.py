import string
import secrets
import pyperclip

# user class starts here
class User:
    """
    class that generates new instances of user
    """

    #empty user list
    users_list = [] 

    def __init__(self, first_name,last_name,email,phone_number, password):
        
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password
    
    #save user
    def save_user(self):
        '''
        save_user method saves objects into user_list
        '''
        
        User.users_list.append(self)

    #displaying all saved users
    @classmethod
    def display_user(cls):
        '''
        this method returns user details.
        '''
        return cls.users_list    

    #deleting user
    def delete_user(self):
        '''
        function to delete user info
        '''
        User.users_list.remove(self)    
    

# class for Credential starts here
class Credential:
    '''
    this is the class to create account credentials, generate password and save the users information
    '''
    credential_list = []
    user_credentials_list = []

    @classmethod
    def check_user(cls,first_name, password):
        '''
        function that checks if the user name and password entered matches with the one on user_list.
        '''
        current_user = ""
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
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

    def generate_password(self, pass_len=5):
        password_chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(password_chars) for i in range(int(pass_len)))
      
    @classmethod
    def find_by_socialmedia(cls, socialmedia):
        '''
        function to find whether the user credentials exist
        '''
        for credential in cls.credential_list:
            if credential.socialmedia == socialmedia:
                
                return credential

    # @classmethod
    # def copy_socialmedia(cls, socialmedia):
    #     '''
    #     method to copy user credentials to the clipboard once user account is entered.
    #     '''
    #     credentials_found =Credential.find_by_socialmedia(socialmedia)
    #     pyperclip.copy(credentials_found.socialmedia)