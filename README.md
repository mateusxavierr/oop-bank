# OOP Bank System

This is a simple Object-Oriented Programming (OOP) bank system developed in Python. It simulates basic banking operations, following clean architecture principles and incorporating key OOP concepts such as abstraction, encapsulation, inheritance and polymorphism.

## 🧱 Project Structure

- `bank_main.py`: Main entry point of the application.
- `bank_module.py`: Contains class definitions and core business logic (Bank, Customer, Account, etc.).
- `bank_ui.py`: Handles user interface strings and menus.
- `json/customers_database.json`: Stores customer data persistently.

## 💡 Features

- Customer registration and login
- Checking and Savings account creation
- Deposit and withdrawal operations
- Account deletion (Danger Zone)
- JSON-based persistent storage
- Clear separation of responsibilities

## 📌 OOP Principles Applied

- **Encapsulation**: Methods and attributes grouped logically in each class.
- **Inheritance**: `CheckingAccount` and `SavingsAccount` inherit from abstract `Account`.
- **Polymorphism**: Different account types implement `withdraw()` with distinct behavior.
- **Abstraction**: `Account` is an abstract base class.

## 🛠️ How to Run

1. Clone the repository:

       git clone https://github.com/mateusxavierr/OOP_bank.git
       cd OOP_bank

2. Run the project:

       python3 bank_main.py

## 📁 Folder Structure

       OOP_bank/
       ├── bank_main.py
       ├── bank_module.py
       ├── bank_ui.py
       ├── json/
       │   └── customers_database.json
       ├── README.md
       └── TODO.md


## 📌 Notes

- All data is stored locally in the `json/` folder.
- JSON file path is dynamically handled using `os.path.join()` for cross-platform compatibility.