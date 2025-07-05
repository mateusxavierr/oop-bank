def type_number():
    return '\nType the number correspondent to your choice: '

def invalid_input():
    return 'Invalid input, try again\n'

def initial_menu():
    return('------- XAVIER BANK -------\n'
            '1 - Create new account\n'
            '2 - Log in your accouny\n'
            '3 - Exit')
    
def login_menu(customer):
    return(f'Welcome {customer.first_name}!\n'
           '1 - Manage checking account\n'
           '2 - Manage savings account\n'
           '3 - Logout\n'
           '4 - Danger zone')

def ask_create_account(account_type):
    return(f'You do not have a {account_type} account yet.\n'
           'Do you want to create one?\n'
           '1 - Yes\n'
           '2 - No')

def account_menu(account_type):
    return (f'----- {account_type.upper()} ACCOUNT -----\n'
            '1 - Check account details\n'
            '2 - Deposit\n'
            '3 - Withdraw\n'
            '4 - Back to menu')

def account_details(account, account_type):
    print(f'{account.capitalize()} account details:\n'
            f'Account number: {account_type.full_account}\n'
            f'Account branch: {account_type.branch}')
    if account_type.balance >= 0:
        print(f'Balance: \033[92m${account_type.balance}\033[0m')

    else:
        print(f'Balance: \033[91m-${-account_type.balance}\033[0m')

    if hasattr(account_type, 'overdraft_limit'):
        print(f'Overdraft limit: \033[91m${account_type.overdraft_limit}\033[0m\n')
        
def danger_zone():
    return('Danger zone: these actions cannot be reversed\n'
           '1 - Delete your checking account\n'
           '2 - Delete your savings account\n'
           '3 - Delete your profile\n'
           '4 - Go back to menu')

def are_you_sure():
    return('Are you sure you want to delete?\n'
           'This action cannot be undone.\n'
           '1 - Yes, continue\n'
           '2 - No, cancel')