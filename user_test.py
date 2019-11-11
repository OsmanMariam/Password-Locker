import unittest
import pyperclip
from user import User, Account


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
        self.new_user = User("Mariam", "Osman", "6969")

    def test__init__(self):
        '''
        Test case to to test if an instance of the object is created
        '''
        self.assertEqual(self.new_user.first_name, "Mariam")
        self.assertEqual(self.new_user.last_name, "Osman")
        self.assertEqual(self.new_user.password, "6969")

    def test_save_user(self):
        '''
        Test to check if in a new user is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)


class TestDetails(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    Args:
        unittest.TestCase: TestCase that helps in creating test cases
    '''

    def test_verify_user(self):
        '''
        Function to verify a user based on their account details
        '''
        self.new_user = User("Mariam", "Osman", "6969")
        self.new_user.save_user()

    def setUp(self):
        '''
        Function to create an account before each test
        '''
        self.new_account = Accounts("Mariam", "Instagram", "mariri", "6969")

    def test__init__(self):
        '''
        Test to if check the initialization/creation of credential instances is properly done
        '''
        self.assertEqual(self.new_credential.user_name, "Mariam")
        self.assertEqual(self.new_credential.site_name, "Instagram")
        self.assertEqual(self.new_credential.account_name, "mariri")
        self.assertEqual(self.new_credential.password, "6969")

    def test_save_account(self):
        '''
        Test to check if the new account inputted is saved into the accounts list
        '''
        self.new_account.save_account()
		Instagram = Account('Mariam','Instagram','mariri','6969')
		Instagram.save_account()

    def tearDown(self):
		'''
		Function to clean up the list after the test case has been executed
		'''
		Accounts.account_list = []
		User.users_list = []




	

	
if __name__ == '__main__':
	unittest.main()
