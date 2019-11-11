import pyperclip
import random
import string


class User:
    users_list = []


    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

        '''
        Class to create new accounts.
        '''


    def save_user(self):
        '''
        Function to save user account details
        '''
        User.users_list.append(self)

    @classmethod
    def verify_users(cls, firstname, password):
        '''
        Method to verify account
        '''
        for user in cls.users_list:
            if user.first_name == firstname and user.password == password:
                return True
        return False


class Account:
    accounts_list = []
    user_account_list = []

    def __init__(self, first_name, site_name, user_name, password):
        '''
        Method to define the properties for each object
        '''

        self.first_name = first_name
        self.site_name = site_name
        self.user_name = user_name
        self.password = password

    def save_account(self):
        '''
        Function to save a newly created user instance
        '''

        Account.accounts_list.append(self)
    def delete_account(self):
        '''
        Function to delete passwords
        '''
        Account.accounts_list.remove(self)





        
        


