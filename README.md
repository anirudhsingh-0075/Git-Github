The objective of this project was to create a banking application using Python 3 that allows customers to open an account, deposit,
withdraw, transfer money and check their bank account data which would be saves in a text file.

The code that I have written fulfills all the requirements of the project specifications.
-Account creation: It generates accounts with unique auto-incrementing account numbers starting from 1001.
-Core banking functions: There are also the deposit, withdraw, transfer and balance operations using dedicated python functions.
-Minimum balance rule: The code also enforces a minimum balance rule of 500 to always remain in account regardless of withdrawal or transfer operations.
-Input validation: Measures have also been taken to block invalid value inputs.
-Persistent storage: Persistent storage is used to save all data sequentially so that no data is lost if the program is closed.

4 core programming concepts were used as specified in the project instrutions.
1. Loops: A 'while true' loop drives the main console menu allowing us to perform multiple operations continuously until we choose to exit.
2. Functions: The code is modularized using the 'def' keyword and some functions handle specific tasks like 'load_accounts()', transfer_money(),' to make the code cleaner and esier to debug.
3. Conditions: if-elif-else statements are used to route the menu options and perform logical checks such as verifying an account or if the withdrwl amount is higher than the balance.
4. File Handling: The program reads fron ("r") and writes to ("w") to a text file (bank.txt).

The test cases have also been passed successfully.

Instructions to run
1. Ensure Python 3 is installed on system
2. open the terminal.
3. run the script.
4. follow the on screen menu (1-6) to interact with the banking system.
