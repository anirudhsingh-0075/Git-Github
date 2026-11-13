# Project Summary and Test Results

## 1. Test Case Verifications
Below are the screenshots verifying that the Simple Banking System successfully passes all four required test cases.

### Test Case 1: Normal Input
**Action:** Created account for 'Anil' with a deposit of 2000.
**Expected:** Account created. A/C No: 1001 | Balance: 2000
![Test Case 1 Output](<Screenshot (33).png>)

### Test Case 2: Boundary / Minimum Input
**Action:** Withdrew 1500 from Account 1001 (Balance 2000).
**Expected:** Withdrawal successful. Balance: 500
![Test Case 2 Output](<Screenshot (34).png>)

### Test Case 3: Invalid Input
**Action:** Attempted transfer to non-existent Account 9999.
**Expected:** Account 9999 not found. Transfer cancelled.
![Test Case 3 Output](<Screenshot (37).png>)

### Test Case 4: Different Valid Scenario
**Action:** Transferred 1000 from Account 1002 to Account 1001.
**Expected:** Transfer successful. 1002 balance: 2000 | 1001 balance: 3000
![Test Case 4 Output](<Screenshot (38).png>)

---

## 2. Difficulties Faced During Development

While building this project, I encountered several technical problems:

*   **Version Control and GitHub Integration:** One of the most significant challenges was navigating Git and GitHub using VS Code. I encountered initial issues with local workspace configurations, such as accidentally saving the Python file inside the hidden `.git` system folder, which caused Git to ignore it. I also had to troubleshoot branch naming conflicts (`main` vs `master`) and learn how to properly link a local repository to a remote GitHub URL using the terminal. 
*   **Exact Output Formatting:** The project required the terminal output to match the test cases exactly. Because Python naturally converts division and some math operations to floats (e.g., `2000.0`), I had to implement custom formatting functions to cleanly display whole numbers as integers (`2000`) while preserving decimal logic behind the scenes.
*   **Persistent File Handling:** Reading and writing to `bank.txt` required careful string manipulation. Extracting the data using `.split(",")` meant all numbers were read as text. Converting these strings back into integers and floats without crashing the program—especially when dealing with empty lines or potential user input errors—required the careful use of `try-except` blocks and data validation.