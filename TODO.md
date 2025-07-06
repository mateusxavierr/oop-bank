# ✅ TODO — OOP Bank System (Step-by-Step)

## 👣 Step-by-Step Implementation

### 🧱 Setup & Structure
- [x] Created main script (`bank_main.py`)
- [x] Created module for classes and business logic (`bank_module.py`)
- [x] Created UI handler (`bank_ui.py`)
- [x] Created `json/` folder for persistent storage

### 🧑‍💼 Customer System
- [x] Implemented CPF and PIN-based customer registration
- [x] Validated CPF, PIN, name, and age input using lambdas and a centralized `Validate` class
- [x] Saved new customer as a dictionary with empty account placeholders
- [x] Wrote customer data to JSON file
- [x] Loaded and parsed customer data into usable structures at runtime
- [x] Handled login with 4-attempt retry logic

### 🏦 Account Management
- [x] Created abstract `Account` class with `withdraw` method
- [x] Implemented `CheckingAccount` with overdraft support
- [x] Implemented `SavingsAccount` without overdraft
- [x] Allowed account creation only if it didn’t already exist
- [x] Added method to create and link accounts to customers using `open_account()`
- [x] Converted account objects to dictionaries and updated customer record in JSON
- [x] Prevented re-creation of existing accounts

### 💰 Operations
- [x] Deposit method with balance update and persistence
- [x] Withdrawal method with overdraft logic for checking accounts
- [x] Balance display with color formatting
- [x] Added display of full account info including overdraft for CC

### 🧨 Danger Zone
- [x] Delete checking account (sets dict to `{}`, updates JSON)
- [x] Delete savings account (same logic)
- [x] Delete customer (removes entry by index)
- [x] Removed need to call `update_customer_data()` after deletion
- [x] Adjusted danger zone flow to avoid using deleted objects

### 🧠 Bank Class
- [x] Created `Bank` class to aggregate customer/account logic
- [x] Moved responsibilities like underage check and data coordination to Bank

### 🔧 Utilities & Persistence
- [x] Created `DatabaseManager` to read/write/update JSON
- [x] Added `update_database()` method to persist changes
- [x] Used dynamic JSON path to avoid absolute system paths

### 🧼 Clean Code & Documentation
- [x] Commented code throughout modules
- [x] Wrote `README.md` with project overview, features, OOP principles, and usage
- [x] Wrote this detailed `TODO.md` to document each step
- [x] Followed conventional commits
- [x] Used Git branches: `main`, `develop`, `docs`, `chore/dynamic-json-path`