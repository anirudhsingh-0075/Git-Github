# Project Report: Simple Banking System

## 1. Problem Statement

The objective of this project is to create a console-based banking application in Python 3 that allows customers to open an account, deposit, withdraw, transfer money, and check their balance, with all account data persistently stored in a text file.

## 2. Features Implemented

This solution strictly fulfills all the bare minimum requirements outlined in the project specifications:

* **Account Creation:** Generates accounts with unique, auto-incrementing account numbers starting from `1001`.


* **Core Banking Functions:** Fully implements deposit, withdrawal, transfer, and balance enquiry operations using dedicated Python functions.


* **Minimum Balance Rule:** Enforces a strict minimum balance rule, ensuring that Rs. 500 must always remain in an account during creation, withdrawal, and transfer operations.


* **Input Validation:** Validates all user inputs to prevent program crashes from non-numeric characters and blocks invalid transfers to non-existent accounts.


* **Persistent Storage:** Stores and loads all account data sequentially using a local `bank.txt` file, ensuring no data is lost when the program closes.



## 3. Core Programming Concepts Applied

The logic was built using the four core programming concepts specified in the curriculum:

* **Loops:** A `while True` loop drives the main console menu, allowing the user to perform multiple operations continuously until they explicitly choose to exit.
* **Functions:** The system is heavily modularized using the `def` keyword. Distinct functions handle specific tasks (e.g., `load_accounts()`, `transfer_money()`), making the code clean, reusable, and easy to debug.
* **Conditions:** `if-elif-else` statements are used to route menu choices and perform crucial logical checks, such as verifying if an account exists or if a withdrawal exceeds the allowed minimum balance.
* **File Handling:** The program reads from (`"r"`) and writes to (`"w"`) a text file (`bank.txt`). Data is parsed using the string `.split(",")` method to load balances into memory and reformatted to save updates instantly.

## 4. Test Cases & Expected Outputs

The application has been successfully tested against the required problem scenarios:

**Test Case 1: Normal Input**
Menu option 1 (Create account)

Name: Anil
 Opening deposit: 2000 
Account created. A/C No: 1001
Balance: 2000 
Passed

**Test Case 2: Boundary Input**
Account 1001 has balance 2000<
Withdraw 1500 
Withdrawal successful. Balance: 500
Passed

**Test Case 3: Invalid Input** 
Account 1001 has balance 2000
Transfer 100 to account 9999
 Account 9999 not found. Transfer cancelled.
Passed 

**Test Case 4: Valid Scenario** 
Accounts: 1001 (2000), 1002 (3000)
Transfer 1000 from 1002 to 1001
 Transfer successful.
1002 balance: 2000
1001 balance: 3000 
Passed 

## 5. Instructions to Run

1. Ensure Python 3 is installed on the system.
2. Open a terminal or command prompt in the project folder.
3. Run the script using the command: `python One.py`.
4. Follow the on-screen numeric menu (1-6) to interact with the banking system.