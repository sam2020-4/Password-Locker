import unittest #Importing the unittest module
from user import User
from user import Credential 
import pyperclip

class testUser (unittest.TestCase):  

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_user = User("sam", "matta", "1234") #create a user object

    def test__init(self):
        '''
        test__init test casre to test if the object is initialized property.
        '''

        self.assertEqual(self.new_user.u_name,"sam")
        self.assertEqual(self.new_user.l_name,"matta")
        self.assertEqual(self.new_user.password,"1234")

    def tearDown(self):
        Credential.credentials_list = []
        User.user_list = []
    

    #save new user
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saves into users list.
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)
    
    #testing delete function here
    def test_delete_user(self):
        '''
        function to delete user to test if we can remove a user from our user_list
        '''
        self.new_user.save_user()
        test_user = User("sam", "matta", "1234")
        test_user.save_user()

        test_user.delete_user()
        self.assertEqual(len(User.user_list), 1)    

    #display user credentials
    def test_display_user(self):
        '''
        this methed enables the application to displays list of all users saved.
        '''
        self.assertEqual(User.display_user(),User.user_list)

# conducting test for the Credential class, 
# starting from initializing variables, saving, deleting, finding social media account
# and impementing copy method.
class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential("sam", "twitter", "12345")
    
    def test__init__(self,):
        self.assertEqual(self.new_credential.user_name, "sam")
        self.assertEqual(self.new_credential.socialmedia, "twitter")
        self.assertEqual(self.new_credential.password, "12345")

# testing credentials
    def tearDown(self):
        Credential.credential_list = []
        User.user_list = []

    def test_save_credentials(self):
        self.new_credential.save_credentials()
        twitter = Credential("sam", "twitter", "12345")
        twitter.save_credentials()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credentials(self):
        self.new_credential.save_credentials()
        twitter = Credential("sam", "twitter", "12345")
        twitter.save_credentials()
        twitter.delete_credentials()
        self.assertEqual(len(Credential.credential_list), 1)

    



if __name__ == '__main__':
    unittest.main()