# DATA ANALYTICS LAB CIA 1
# MAILING SYSTEM

This repository contains a simple command-line mailing system implemented in Python. This system allows users to create email accounts, log in, send and receive emails, and open their inboxes and outboxes.

# Features
The features in the program are-
1. Create a new account- This feature allows users to create a new email account by providing their email and password.
2. Login- This feature allows users to login into their account by entering their email and password.
3. Send Email- This feature allows users to send emails to other users by entering the receiver's email, subject of the email, and message of the email.
4. Open Inbox- This feature allows users to open up their inboxes and view the emails that they have received.
5. Open Outbox- This feature allows users to open up their outboxes and view the emails that they have sent.
6. Logout- This feature allows users to log out of their account.

# Packages
To run this program, the following packages must be installed on your system-
1. 'csv' module: This module is used for reading and writing csv files.

# Usage
The program will execute by displaying this menu-
1. Create a new account
2. Login
0. Exit
The user will be asked to enter their choice, by typing in 1,2, or 0.
If the user chooses 0 to exit, the program will be terminated.
If the user chooses 1 to create a new account, the user will be asked to enter the new account's email and password. If the email entered already exists, then the user will be shown a warning message. If the email entered does not already exist, then the user's new account will be created.
If the user chooses 2 to login, the user will be asked to enter their email and password. If the email and password are incorrect, then the user will be shown a warning message. If the email and password are correct, the user will be logged into their account.
After the user is logged in, they are shown the following menu-
1. Send Email
2. Open Outbox
3. Open Inbox
4. Logout
The user will be asked to enter their choice, by typing in 1,2,3, or 4.
If the user chooses 4 to logout, then the user will be logged out of their account, and they will be shown the main menu.
If the user chooses 1 to send an email, they will be asked to enter the receiver's email, subject of the email and message of the email. If the receiver's email entered by the user is not valid, then the user will be shown a warning message. If the receiver's email is valid, then the email will be sent. The email will be added to the user's outbox, and the receiver's inbox.
If the user chooses 2 to open their outbox, all the emails in their outbox is shown.
If the user chooses 3 to open their inbox, all the emails in their inbox is shown.

# Files created
The data is stored in the following csv files-
1. 'EmailDetails.csv' : This file contains the emails and passwords of all the users.
2. 'Inbox.csv' : This file contains the emails of the users along with all the emails in their inbox.
3. 'Outbox.csv' : This file contains the emails of the users along with all the emails in their outbox.

# Functions
1.'createAccount(email,password)' : This function creates a new email account by adding the email and password to the 'EmailDetails.csv' file. It first checks if the email already exists in the file. If it exists already, the function returns without creating a new account and the user is given a warning message. Otherwise, it appends the email and password to the file, and successfully creates a new account.

2.'addToFiles(email)' : This function appends the given email to the 'Inbox.csv' and 'Outbox.csv' files. It reads the existing rows from each file, appends the email to the existing rows, and then writes the updated rows back to the files.

3.'addColName()' : This function adds column names to the 'EmailDetails.csv' file if they are not already present. It checks if the first row of the file contains the column names 'Email' and 'Password'. If not, it writes the column names as the first row of the file.

4.'login(email,password)' : This function peforms the login process by checking if the given email and password match an existing account in the 'EmailDetails.csv' file. It reads each row in the file and compares the email and password with the provided credentials. If a match is found, the function returns 'True', and successfully logs in. Otherwise, it returns 'False'. If login is successful, the user is shown a new menu including options to send emails, and opening inbox and outbox of the user.

5.'check_email_existence(email)' : This function checks if the given email exists in 'Inbox.csv' file and 'Outbox.csv' file. If it exists in both, it returns 'True'. Otherwise, it returns 'False'.

6.'sendEmail(user,receiver,subject,msg)' : This function sends an email from the user to the receiver. It first checks if the receiver's email exists in 'Inbox.csv' and 'Outbox.csv' files using 'check_email_existence(email)' function. If the email does not exist, the user is given a warning error. Otherwise, it appends the email information to the user's row in the 'Inbox.csv' file, and the receiver's row in the 'Outbox.csv' file.

7.'readInbox(email)' : This function reads and displays the emails received by the given email address. It reads the 'Inbox.csv' file and checks each row for a matching email address. If a match is found, it prints all the email details. If no emails are found, it prints a message indicating that no emails have been received yet.

8.'readOutbox(email)' : This function reads and displays the emails sent by the given email address. It reads the 'Outbox.csv' file and checks each row for a matching email address. If a match is found, it prints all the email details. If no emails are found, it prints a message indicating that no emails have been sent yet.

9.'logout()' : This function logs the user out of their account, displays a message indicating the successful logout, and brings the user back to the main menu.

10.'main()' : This is the main function that drives the mailing system. It creates/opens the required csv files. It calls the addColName() function as well. It presents a menu to the user and performs the corresponding actions based on the user's choices.

