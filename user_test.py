import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    Args:
        unittest.TestCase: TestCase that helps in creating test cases
    '''

    def setUp(self):
        '''
        Method to run by creating new account before each test case
        '''
        self.new_user = User("Mariam","Osman","6969")

    def test__init__(self): 
        '''
        Test case to to test if an instance of the object is created
        '''
        self.assertEqual(self.new_user.first_name,"Mariam")
        self.assertEqual(self.new_user.last_name,"Osman")        
        self.assertEqual(self.new_user.password,"6969")        

    def test_save_user(self):
        '''
        Test to check if in a new user is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

