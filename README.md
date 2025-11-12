# Bank Management System
 This is a command-line application for a basic bank system that allows users to perform various operations such as opening a new account, depositing money, withdrawing money, checking the account balance, getting account details and closing an account. The application is written in Python and uses MySQL database to store and retrieve data.

# Requirements
1.Python 3.x
2.MySQL Connector for Python (`pip install mysql-connector-python`)
3.MySQL Server

# Installation
1. Install Python and MySQL Connector for Python.
2. Install MySQL Server and create a database named `bank_sys`.
3. Import the`bank_sys.sql` file from the repository into the bank_sys database.
4. Open the `bank_system.py` file in a text editor.
5. Update the MySQL database connection details (host, user, password) as required.
6. Save the file.

# Usage
1. Open a command prompt or terminal window.
2. Navigate to the directory where the `bank_system.py` file is saved.
3. Run the command `python bank_system.py` to start the application.
4. Follow the on-screen prompts to perform the desired operations.

# Demo
Here's a quick demo of how the application works:

```bash
********************************************
<><><><><><><><>[  MAIN MENU ]<><><><><><><>
********************************************
            1.OPEN NEW ACCOUNT
            2.DEPOSIT AMOUNT
            3.WITHDRAW AMOUNT
            4.BALANCE ENQUIRY
            5.ACCOUNT DETAIL
            6.CLOSE ACCOUNT
********************************************

Enter Your Choice >>> 1

*************OPEN NEW ACCOUNT*************
Enter Account No.:- 1001
Enter Name :- Rahul
Enter Date of Birth :- 2000-01-01
Enter Address :- 123 Pune, Maharashtra
Enter Mobile No.:- 1234567890
Enter Opening Balance :- 1000
Congratulaions Account Open Successfully

*********************************************
<><><><><><><><>[  MAIN MENU ]<><><><><><><>
*********************************************
            1.OPEN NEW ACCOUNT
            2.DEPOSIT AMOUNT
            3.WITHDRAW AMOUNT
            4.BALANCE ENQUIRY
            5.ACCOUNT DETAIL
            6.CLOSE ACCOUNT
*********************************************

Enter Your Choice >>> 4

**************BALANCE ENQUIRY**************
	Enter Account No :- 1001
******************BALANCE*******************
	Current Balance is RS 1000

*********************************************
<><><><><><><><>[  MAIN MENU ]<><><><><><><>
*********************************************
            1.OPEN NEW ACCOUNT
            2.DEPOSIT AMOUNT
            3.WITHDRAW AMOUNT
            4.BALANCE ENQUIRY
            5.ACCOUNT DETAIL
            6.CLOSE ACCOUNT
*********************************************

Enter Your Choice >>> 2

**************DEPOSIT AMOUNT**************
Enter Amount :- 500
Enter Account No :- 1001

*********************************************
<><><><><><><><>[  MAIN MENU ]<><><><><><><>
*********************************************
            1.OPEN NEW ACCOUNT
            2.DEPOSIT AMOUNT
            3.WITHDRAW AMOUNT
            4.BALANCE ENQUIRY
            5.ACCOUNT DETAIL
            6.CLOSE ACCOUNT
*********************************************

Enter Your Choice >>> 4

**************BALANCE ENQUIRY**************
	Enter Account No :- 1001
******************BALANCE*******************
	Current Balance is RS 1500

*********************************************
<><><><><><><><>[  MAIN MENU ]<><><><><><><>
*********************************************
            1.OPEN NEW ACCOUNT
            2.DEPOSIT AMOUNT
            3.WITHDRAW AMOUNT
            4.BALANCE ENQUIRY
            5.ACCOUNT DETAIL
            6.CLOSE ACCOUNT
*********************************************

Enter Your Choice >>> 3

**************WITHDRAW AMOUNT**************
Enter Withdraw Amount :- 1000
Enter Account No :- 1001

*********************************************
<><><><><><><><>[  MAIN MENU ]<><><><><><><>
*********************************************
            1.OPEN NEW ACCOUNT
            2.DEPOSIT AMOUNT
            3.WITHDRAW AMOUNT
            4.BALANCE ENQUIRY
            5.ACCOUNT DETAIL
            6.CLOSE ACCOUNT
*********************************************

Enter Your Choice >>> 4

**************BALANCE ENQUIRY**************
	Enter Account No :- 1001
******************BALANCE*******************
	Current Balance is RS 500

*********************************************
<><><><><><><><>[  MAIN MENU ]<><><><><><><>
*********************************************
            1.OPEN NEW ACCOUNT
            2.DEPOSIT AMOUNT
            3.WITHDRAW AMOUNT
            4.BALANCE ENQUIRY
            5.ACCOUNT DETAIL
            6.CLOSE ACCOUNT
*********************************************

Enter Your Choice >>> 5

***********CHECK ACCOUNT DETAILS************
	Enter Account No :- 1001
******************DETAILS*******************
1001  |  Rahul  |  2000-01-01  |  123 Pune, Maharashtra  | 1234567890 |  500  |

Enter Your Choice >>> 6
        Enter Account No :- 1001

.......Account Deleted Successfully.........

```

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.
