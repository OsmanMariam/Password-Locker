import pyperclip
import random
import string


class User:
    users_list=[]
    def __init__(self,first_name,last_name,password):
        self.first_name= first_name
        self.last_name= last_name
        self.password= password

    '''
    Class to create new accounts.
    '''
    def save_user(self):
        '''
        Function to save user account details
        '''
        User.users_list.append(self)

# class Credential:
# 	'''
# 	Class to create  account credentials, generate passwords and save their information
# 	'''
# 	# Class Variables
# 	credentials_list =[]
# 	user_credentials_list = []          
