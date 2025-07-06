from abc import ABC, abstractmethod
import bank_ui as ui
import json
import random

#
# Validates user input during registration and login
class Validate:
    # Checks if the full name includes name and surname
    def full_name_check(self, answer):
        try:
            name, surname = answer.split(' ', 1)

        except Exception:
            print(ui.invalid_input())
            return False

        else:
            self.name = name
            self.surname = surname
            return True
    
    # Validates if age is a number and 18 or older
    def age_check(self, answer):        
        try:
            age = int(answer)

        except Exception:
            print(ui.invalid_input())
            return False

        else:
            if age >= 18:
                self.age = age
                self.underage = False
                return True
            
            elif age < 18 and age >= 0:
                print('You need to be 18 or older to create an account\n')
                self.underage = True
                return True
            
            else:
                print(ui.invalid_input())
                return False

    # Helper method for CPF validation (digit calculation)
    @staticmethod
    def _verify_cpf_digits(qtt_multiplied_numbers, multiplicator, cpf):
        sum_ = 0
        for num in cpf[:(qtt_multiplied_numbers)]:
            multiplication = (int(num) * multiplicator)
            multiplicator -= 1
            sum_ += multiplication

        remainder = (sum_ * 10 % 11)
        if remainder > 9:
            digit = 0
        else: 
            digit = remainder

        return digit

    # Validates CPF format and uniqueness
    def cpf_check(self, database_list, answer):
        if len(answer) == 11:
            try:
                first_digit = self._verify_cpf_digits(9, 10, answer)
                second_digit = self._verify_cpf_digits(10, 11, answer)

            except Exception:
                print(ui.invalid_input())
                return False

            else:
                if first_digit == int(answer[9]) and second_digit == int(answer[10]) and len(answer) == 11:
                    for dictionary in database_list:
                        if dictionary['cpf'] == answer:
                            print('This CPF is already registered\n')
                            return False
                    
                    self.cpf = answer
                    return True
                
                else:
                    print(ui.invalid_input())
                    return False

        else:
            print(ui.invalid_input())
            return False

    # Stores a valid 4-digit PIN
    def pin_first(self, answer):
        if len(answer) == 4 and answer.isdigit():
            self.pin = answer
            return True
        
        else:
            print(ui.invalid_input())
            return False
        
    # Confirms the repeated PIN matches
    def pin_second(self, answer):
        if answer == self.pin:
            return True
        
        else:
            print(ui.invalid_input())
            return False
        
#
# Handles reading, writing, and updating customer JSON database
class DatabaseManager:
    def __init__(self, path):
        self.path = path

    # Loads all customers from the JSON file
    def load_database(self):
        try:
            with open(self.path, 'r') as f:
                return json.load(f)
            
        except Exception:
            return []

    # Appends a new customer to the database
    def customer_data_dump(self, database_list, customer_dict):
        try:
            with open (self.path, 'r') as f:
                database_list = json.load(f)

        except Exception:
            database_list = []

        database_list.append(customer_dict)

        with open(self.path, 'w') as f:
            json.dump(database_list, f, indent=4)

    # Updates an existing customer's data in the database
    def update_database(self, database_list, customer_dict):
        for n, dictionary in enumerate(database_list):
            if dictionary['cpf'] == customer_dict['cpf']:
                database_list[n] = customer_dict
                break

        with open(self.path, 'w') as f:
            json.dump(database_list, f, indent=4)

#
# Abstract base class for all account types
class Account(ABC):
    # Initializes account with random number, digit, branch
    def __init__(self, balance=0):
        self.number = random.randint(1000000, 9999999)
        self.digit = random.randint(0, 9)
        self.branch = random.randint(1000, 9999)
        self.balance = balance
        self.full_account = f'{self.number}-{self.digit}'

    # Handles deposit input and updates balance
    def deposit(self):
        depositing = True
        while depositing:
            choice = input('Type how much you want to deposit: ')

            try:
               amount = float(choice)

            except Exception:
                print(ui.invalid_input())
            
            else:
                if amount > 0:
                    self.balance += amount
                    print('Operation processed.\n'
                          f'Your balance is now \033[92m${self.balance}\033[0m\n')
                    depositing = False
                
                else:
                    print('Your deposit must be above $0\n')
                
    # Abstract method for withdrawal logic
    @abstractmethod
    def withdraw(self):
        pass

    # Abstract method for recreating account from dict
    @classmethod
    @abstractmethod
    def from_dict(cls, dictionary):
        pass

#
# Concrete class for savings accounts
class SavingsAccount(Account):
    # Withdrawal logic without overdraft
    def withdraw(self):
        while True:
            choice = input('Type how much you want to withdraw: ')

            try:
                amount = float(choice)

            except Exception:
                print(ui.invalid_input())
                continue

            else:
                if amount <= 0:
                    print('Your withdraw must be above $0\n')

                else:
                    balance = self.balance - amount

                    if balance < 0:
                        print('Operation not processed.\n'
                                'You do not have sufficient funds to withdraw this amount.\n')
                        break
                    
                    else:
                        self.balance = balance
                        print(f'Operation processed.\nYour balance now is \033[92m${self.balance}\033[0m\n')
                        break
            
    # Creates account instance from dictionary
    @classmethod
    def from_dict(cls, dictionary):
        instance = cls()
        instance.number = dictionary['number']
        instance.digit = dictionary['digit']
        instance.branch = dictionary['branch']
        instance.full_account = dictionary['full_account']
        instance.balance = dictionary['balance']
        return instance

#
# Concrete class for checking accounts with overdraft support
class CheckingAccount(Account):
    # Initializes account with optional overdraft limit
    def __init__(self, balance=0, overdraft_limit=1000):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    # Withdrawal logic that may use overdraft
    def withdraw(self):
        while True:
            choice = input('Type how much you want to withdraw: ')

            try:
                amount = float(choice)

            except Exception:
                print(ui.invalid_input())
                continue

            else:
                if amount <=0:
                    print('Your withdraw must be above $0\n')
                
                else:
                    balance = self.balance - amount

                    if balance >= 0:
                        self.balance = balance
                        print(f'Operation processed.\nYour balance now is \033[92m${self.balance}\033[0m\n')
                        break
                    
                    elif balance >= -self.overdraft_limit:
                        print('You do not have sufficient funds to withdraw this amount.\n'
                            'You can use your overdraft to get a loan:\n'
                            f'Your balance will be: \033[91m-${-balance}\033[0m\n'
                            'Do you wish to use the overdraft?\n'
                            '1 - Yes\n'
                            '2 - No')
                        choice = input(ui.type_number())

                        if choice == '1':
                            self.balance = balance
                            print(f'Operation processed.\nYour balance is now \033[91m-${-self.balance}\033[0m.\n')
                            break

                        elif choice == '2':
                            print('Operation canceled.\n')
                            break

                        else:
                            print(ui.invalid_input())
                
                    else:
                        print('Operation not processed.\n'
                            'This amount exceeds your balance and your overdraft limit.\n')
                        break

    # Creates account instance from dictionary
    @classmethod
    def from_dict(cls, dictionary):
        instance = cls()
        instance.number = dictionary['number']
        instance.digit = dictionary['digit']
        instance.branch = dictionary['branch']
        instance.full_account = dictionary['full_account']
        instance.balance = dictionary['balance']
        instance.overdraft_limit = dictionary['overdraft_limit']
        return instance
    
#
# Abstract base class for people
class Pearson(ABC):
    # Initializes name and surname
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    # Returns first name
    @property
    def first_name(self):
        return self.name
    
    # Returns last name
    @property
    def last_name(self):
        return self.surname

#
# Concrete class for customers
class Customer(Pearson):
    # Initializes customer attributes
    def __init__(self, name, surname, age, cpf, pin, checking_account={}, savings_account={}):
        super().__init__(name, surname)
        self.age = age
        self.cpf = cpf
        self.pin = pin
        self.checking_account = checking_account
        self.savings_account = savings_account

    # Returns customer data as dictionary
    def data_dictionary(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'cpf': self.cpf,
            'pin': self.pin,
            'checking_account': self.checking_account,
            'savings_account': self.savings_account
        }

    # Creates a new account and stores it under customer
    def open_account(self, account_type_class, account_type):
        account = account_type_class()
        setattr(self, account_type, {
                'balance': account.balance,
                'number': account.number,
                'digit': account.digit,
                'full_account': account.full_account,
                'branch': account.branch})

        if hasattr(account, 'overdraft_limit'):
            getattr(self, account_type)['overdraft_limit'] = account.overdraft_limit

    # Deletes one of the customer's accounts
    def delete_account(self, account_type):
        setattr(self, account_type, {})

#
# Manages customer creation, authentication, and data persistence
class Bank:
    # Stores references to the database and list
    def __init__(self, database_manager, database_list):
        self.database_manager = database_manager
        self.database_list = database_list

    # Updates the customer in database and refreshes list
    def update_customer_data(self, customer):
        customer_dict = customer.data_dictionary()
        self.database_manager.update_database(self.database_list, customer_dict)
        self.database_list = self.database_manager.load_database()

    # Repeatedly prompts until validator returns True
    def answers(self, question, validator):
        answered_correctly = False

        while not answered_correctly:
            answer = input(question)
            answered_correctly = validator(answer)

    # Asks all required inputs to register a new customer
    def new_customer_questions(self, database_list) -> bool:
            self.validator = Validate()
            self.answers('Enter your full name: ', lambda answer: self.validator.full_name_check(answer))
            self.answers('Enter your age: ', lambda answer: self.validator.age_check(answer))
            if self.validator.underage:
                return False
            self.answers('Enter your CPF: ', lambda answer: self.validator.cpf_check(database_list, answer))
            self.answers('Create a 4-digit PIN: ', lambda answer: self.validator.pin_first(answer))
            self.answers('Repeat your 4-digit PIN: ', lambda answer: self.validator.pin_second(answer))
            return True

    # Creates a Customer instance from validator data
    def create_customer(self):
        v = self.validator
        return Customer(v.name, v.surname, v.age, v.cpf, v.pin)

    # Loads a Customer instance from a dictionary
    def load_customer(self, customer_dict):
        customer = Customer(customer_dict['first_name'],
                            customer_dict['last_name'],
                            customer_dict['age'],
                            customer_dict['cpf'],
                            customer_dict['pin'],
                            customer_dict['checking_account'],
                            customer_dict['savings_account'])
        return customer

    # Handles CPF and PIN authentication
    def authenticate_login(self, database_list):
        self.attempts_pin = 4
        self.answers('Enter your CPF: ', lambda answer: self.login_cpf(database_list, answer))
        self.answers('Enter your 4-digit PIN: ', lambda answer: self.login_pin(database_list, answer))
        return not getattr(self, 'login_failed', False)
    
    # Checks CPF existence and position in database
    def login_cpf(self, database_list, answer):
        if len(answer) == 11 and answer.isdigit():
            for n, dictionary in enumerate(database_list):
                if dictionary['cpf'] == answer:
                    self.dict_position = n
                    return True
                
            print('CPF not found, please create an account.\n')
            return False
        
        else:
            print(ui.invalid_input())
            return False
        
    # Validates input PIN and tracks login attempts
    def login_pin(self, database_list, answer):
        if len(answer) != 4 or not answer.isdigit():
            print(ui.invalid_input())
            return False
        
        elif database_list[self.dict_position]['pin'] == answer:
            print('Logged in with success!\n')
            return True
        
        else:
            self.attempts_pin -= 1

            if self.attempts_pin <= 0:
                print('You ran out of attempts. Your login failed.\n')
                self.login_failed = True
                return True

            else:
                print(f'Wrong PIN. You have {self.attempts_pin} attempts left.\n')
                return False
            
    # Removes the authenticated customer from the database
    def delete_customer(self):
        self.database_list.pop(self.dict_position)
        with open(self.database_manager.path, 'w') as f:
            json.dump(self.database_list, f, indent=4)