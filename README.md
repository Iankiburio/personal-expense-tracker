## Personal Expense Tracker

### Introduction
The Expense Tracker is a Python program that allows users to track their expenses. It utilizes the Peewee library for database management and provides a command-line interface for users to interact with the application. The program allows users to add users and categories, add expenses, view all expenses, get the total expenses, modify category and expense data for a user, and delete users and their associated data.

### Dependencies
In order to run the Expense Tracker code, you will need to install the following dependencies:
- Python (version >= 3.6)
- Pipenv (`pip install pipenv`)
- Peewee (`pip install peewee`)

### Database Setup
The Expense Tracker uses SQLite database to store user, category, and expense information. The database file `expenses.db` will be created automatically when you run the program for the first time.

### Running the Program
To run the Expense Tracker, follow the steps below:

1. Open your terminal or command prompt.
2. Navigate to the directory where the `src.py` file is located.
3. Run the following command to activate the virtual environment:
   ```
   pipenv shell
   ```
4. Execute the program by running the following command:
   ```
   python src.py
   ```
5. The program will display the main menu with a list of options. Choose the desired option by entering the corresponding number.
6. Follow the program prompts and provide the necessary information (e.g., username, expense amount, etc.) to perform the selected operation.

### Functionality
1. **Add User and Category**: This option allows you to add a new user and a corresponding category. The program will prompt you to enter the username and category name.

2. **Add Expense**: This option enables you to add an expense for an existing user and category. Before adding an expense, you need to ensure that at least one user and category have been added. The program will prompt you to enter the expense amount.

3. **View All Expenses**: This option displays all the expenses stored in the database. The expenses will be listed with the username, category, amount, and the date/time added.

4. **Get Total Expenses**: This option calculates and displays the total expenses of all users.

5. **Change Category and Expense Data for a User**: This option allows you to modify the category and expense amount for a specific user. You will need to select a username from the available list and enter the new category name and expense amount.

6. **Delete User and Data**: This option allows you to delete a user and all associated expense data. You will need to select a username from the available list to delete the user.

7. **Exit**: This option terminates the program and returns you to the command prompt.

### Notes
- The Expense Tracker enables the creation of unique usernames and category names. Duplicates will not be allowed.
- The program handles cases where usernames, categories, or expenses do not exist, providing informative error messages.
- The program displays appropriate messages when no expenses or users are found in the database.
- The expenses are ordered by their ID, resulting in a chronological order based on when they were added.
- The expense amounts are stored in Kenyan Shillings (Kshs) and are displayed as such in the program output.

### Conclusion
The Expense Tracker is a useful program for efficiently managing and tracking expenses. It provides various options to add, view, modify, and delete user and expense data. By utilizing the Peewee library and SQLite database, the program ensures efficient and reliable management of expense information.
