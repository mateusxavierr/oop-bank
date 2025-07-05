import bank_module
import bank_ui as ui
customers_database_path = 'OOP_bank/customers_database.json'
database_manager = bank_module.DatabaseManager(customers_database_path)
database_list = database_manager.load_database()
bank = bank_module.Bank(database_manager, database_list)

while True:
    print(ui.initial_menu())
    choice = input(ui.type_number())
    print()

    if choice == '1':
        if not bank.new_customer_questions(database_list):
            continue

        new_customer = bank.create_customer()
        new_customer_data_dict = new_customer.data_dictionary()
        database_manager.customer_data_dump(database_list, new_customer_data_dict)
        database_list = database_manager.load_database()
        print('\nAccount created with success. Log in your account in the menu.\n')

    elif choice == '2':
        if not bank.authenticate_login(database_list):
            continue

        else:
            logged_in = True
            logged_user_index = bank.dict_position
            customer_dict = database_list[logged_user_index]
            customer = bank.load_customer(customer_dict)
            
            while logged_in:
                print(ui.login_menu(customer))
                choice = input(ui.type_number())
                print()

                if choice == '1':
                    if not customer.checking_account:
                        creating_account = True
                        while creating_account == True:
                            print(ui.ask_create_account('checking'))
                            choice = input(ui.type_number())
                            print()

                            if choice == '1':
                                customer.open_account(bank_module.CheckingAccount, 'checking_account')
                                bank.update_customer_data(customer)
                                print('Your checking account was created with success!\n')
                                creating_account = False

                            elif choice == '2':
                                print('Returning to menu\n')
                                creating_account = False

                            else:
                                print(ui.invalid_input())

                    else:
                        checking_account = bank_module.CheckingAccount.from_dict(customer.checking_account)
                        account_menu = True
                        while account_menu:
                            print(ui.account_menu('checking'))
                            choice = input(ui.type_number())
                            print()

                            if choice == '1':
                                ui.account_details('checking', checking_account)

                            elif choice == '2':
                                checking_account.deposit()
                                customer.checking_account['balance'] = checking_account.balance
                                bank.update_customer_data(customer)

                            elif choice == '3':
                                checking_account.withdraw()
                                customer.checking_account['balance'] = checking_account.balance
                                bank.update_customer_data(customer)

                            elif choice == '4':
                                print('Returning to menu\n')
                                account_menu = False

                            else:
                                print(ui.invalid_input())

                elif choice == '2':
                    if not customer.savings_account:
                        creating_account = True
                        while creating_account == True:
                            print(ui.ask_create_account('savings'))
                            choice = input(ui.type_number())
                            print()

                            if choice == '1':
                                customer.open_account(bank_module.SavingsAccount, 'savings_account')
                                bank.update_customer_data(customer)
                                print('Your savings account was created with success!\n')
                                creating_account = False

                            elif choice == '2':
                                print('Returning to menu\n')
                                creating_account = False

                            else:
                                print(ui.invalid_input())

                    else:
                        savings_account = bank_module.SavingsAccount.from_dict(customer.savings_account)
                        account_menu = True
                        while account_menu:
                            print(ui.account_menu('savings'))
                            choice = input(ui.type_number())
                            print()

                            if choice == '1':
                                ui.account_details('savings', savings_account)

                            elif choice == '2':
                                savings_account.deposit()
                                customer.savings_account['balance'] = savings_account.balance
                                bank.update_customer_data(customer)

                            elif choice == '3':
                                savings_account.withdraw()
                                customer.savings_account['balance'] = savings_account.balance
                                bank.update_customer_data(customer)

                            elif choice == '4':
                                print('Returning to menu\n')
                                account_menu = False

                            else:
                                print(ui.invalid_input())

                elif choice == '3':
                    print('Logging out...')
                    logged_in = False

                elif choice == '4':
                    danger_zone = True
                    while danger_zone:
                        print(ui.danger_zone())
                        choice = input(ui.type_number())
                        print()
                    
                        if choice == '1':
                            print(ui.are_you_sure())
                            choice = input(ui.type_number())

                            if choice == '1':
                                customer.delete_account('checking_account')
                                bank.update_customer_data(customer)
                                print('Your checking account has been deleted.\n')

                            elif choice == '2':
                                print('The operation was canceled.\n')

                            else:
                                print(ui.invalid_input())

                        elif choice == '2':
                            print(ui.are_you_sure())
                            choice = input(ui.type_number())

                            if choice == '1':
                                customer.delete_account('savings_account')
                                bank.update_customer_data(customer)
                                print('Your savings account has been deleted.\n')

                            elif choice == '2':
                                print('The operation was canceled.\n')

                            else:
                                print(ui.invalid_input())
                        
                        elif choice == '3':
                            print(ui.are_you_sure())
                            choice = input(ui.type_number())

                            if choice == '1':
                                bank.delete_customer()
                                print('Your account has been deleted, going to main menu.\n')
                                danger_zone = False
                                logged_in = False

                            elif choice == '2':
                                print('The operation was canceled.\n')

                            else:
                                print(ui.invalid_input())

                        elif choice == '4':
                            danger_zone = False
                            print()

                        else:
                            print(ui.invalid_input())

                else:
                    print(ui.invalid_input())
            
    elif choice == '3':
        break

    else:
        print(ui.invalid_input())
