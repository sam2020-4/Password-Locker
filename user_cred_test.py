import unittest #Importing the unittest module
from user import User 

class testUser (unittest.TestCase):

    '''
    Test class that defines test cases for the user classs variable.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_user = User("sam", "matta", "12345") #create a user object

    def test__init(self):
        '''
        test__init test casre to test if the object is initialized propery.
        '''

        self.assertEqual(self.new_user.u_name,"sam")
        self.assertEqual(self.new_user.l_name,"matta")
        self.assertEqual(self.new_user.password,"12345")

    #save new user
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saves into users list.
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)



if __name__ == '__main__':
    unittest.main()