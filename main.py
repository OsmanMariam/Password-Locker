#!/usr/bin/env python3.6
import pyperclip
from user import User
from user import Account

def create_user(firstname,lastname,password):
	'''
	Function to add a new user 
	'''
	new_user = User(firstname,lastname,password)
	return new_user

def save_user(User):
	'''
	Function to save a user
	'''
	User.save_user()


def verify_user(firstname,password):
	'''
	Function that verifies a user
	'''
	return User.verify_users(firstname,password)

def validate_user(first_name,last_name,password):
	'''
	Function to validate a user
	'''
	if first_name=="" or last_name=="" or password=="":
		return False
	else:
		return True	

def create_account(firstname,site_name,account_name,password):
	'''
	Function to create a new account
	'''
	new_account=Account(firstname,site_name,account_name,password)
	return new_account

def save_account(Account):
	'''
	Function to save a new account
	'''
	Account.save_account()
def delete_account(Account):
	'''
	Function to delete account
	'''
	Account.delete_account()

def find_account_bysite(site_name):
	'''
	Function to find ana account
	'''
	return Account.find_account(site_name)

def check_exsisting_account(site_name):
	'''
	Function to check for an existing account
	'''
	return Account.existing_account(site_name)



def main():
	print('Welcome to Password Locker.')
	while True:
		print('\n ca-Create an Account \n li-Log In  \n ex-Exit ')
		short_code = input('Enter a choice: ')
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print('To create a new account:')
			first_name = input('Enter your first name ')
			last_name = input('Enter your last name')
			password = input('Enter your password')
			save_user(create_user(first_name,last_name,password))
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')

		elif short_code == 'li':
			print('To login, enter your account details:')
			user_name = input('Enter your first name')
			password = input('Enter your password' )
			# user_exists = verify_user(user_name,password)
			if verify_user(user_name,password):
				print(f'Welcome {user_name}. Please choose an option to continue.')
				while True:
					print('\n ca-Create an Account \n da-Display Accounts \n dlt- Delete Account \n ex-Exit' )
					short_code = input('Enter a choice: ')
					if short_code == 'ex':
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'ca':
						print('Enter your  external account details:')
						first_name= input('Enter your first name')
						site_name = input('Enter the site\'s name- ')
						user_name = input('Enter your user_name ')
						while True:
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ')
							if psw_choice == 'ep':
								password = input('Enter your password: ')
							elif psw_choice == 'gp':
								password = user_name[:4]+"6951de"
							save_account(create_account(first_name,site_name,user_name,password))
							print(' ')
							print(f'Account Created: Site Name: {site_name} - Account Name: {user_name} - Password: {password}')
							print(' ')
							break
					elif short_code == 'da':
						if display_account() !='':
							print('Here is a list of all your accounts')
							for account in display_account():
								print(f'Site Name: {account.site_name} - Account Name: {account.user_name} - Password: {account.password}')	
						else:
							print("You don't have any accounts saved yet")


					elif short_code=="dlt":
						print("Enter account you would like to delete")
						to_delete=input() 
						if check_exsisting_account(to_delete):
							del_acc=find_account_bysite(to_delete)
							delete_account(del_acc)
							print("Account deleted")
						else:
							print("No account found")	
								

					
					
					else:
						print('Oops! Wrong option entered. Try again.')

			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		else:
			
			
			print('Oops! Wrong option entered. Try again.')
				






if __name__ == '__main__':
	main()