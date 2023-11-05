from peewee import *
from peewee import fn
from datetime import datetime

db = SqliteDatabase("expenses.db")

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

class Category(BaseModel):
    name = CharField(unique=True)

class Expense(BaseModel):
    category = ForeignKeyField(Category)
    user = ForeignKeyField(User)
    amount = FloatField()
    timestamp = DateTimeField(default=datetime.now)

def create_tables():
    with db:
        db.create_tables([User, Category, Expense, BaseModel])

def add_user_category():
    username = input("Enter username: ")
    category_name = input("Enter category name: ")

    user, created = User.get_or_create(username=username)
    category, created = Category.get_or_create(name=category_name)

    print(f"User '{user.username}' and Category '{category.name}' added.")

    return user, category

def add_expense(expense_data, category, user):
    amount_in_kshs = expense_data['amount']
    currency = "Kshs"  

    expense = Expense.create(
        category=category,
        user=user,
        amount=amount_in_kshs
    )
    
    print(f"Expense added successfully. Amount: {amount_in_kshs} {currency}")

    return expense

def print_expenses(expenses):
    currency = "Kshs"  

    for expense in expenses:
        amount_in_kshs = expense.amount
        print(f"Username: {expense.user.username}, Category: {expense.category.name}, Amount: {amount_in_kshs} {currency}, Date/Time Added: {expense.timestamp}")


def view_all_expenses():
    expenses = (Expense
                .select(Expense, User.username)
                .join(User)
                .switch(Expense)
                .join(Category)
                .order_by(Expense.id))

    if expenses:
        print_expenses(expenses)
    else:
        print("No expenses found.")

def get_total_expenses():
    currency = "Kshs"  

    total_expenses = Expense.select(fn.Sum(Expense.amount)).join(Category).scalar()
    total_expenses = total_expenses if total_expenses else 0  # Handling None value

    if total_expenses:
        print(f"Total expenses: {total_expenses} {currency}")
    else:
        print("No expenses found.")


def delete_user(username):
    try:
        user = User.get(User.username == username)
    except User.DoesNotExist:
        print(f"User '{username}' does not exist.")
        return

    with db.atomic():
        Expense.delete().where(Expense.user == user).execute()
        user.delete_instance()

    print(f"User '{username}' and associated expenses deleted.")

def main_menu():
    is_user_category_added = False  # checks if user and category are added

    while True:
        print("=== Expense Tracker ===")
        print("1. Add User and Category")
        print("2. Add Expense")
        print("3. View All Expenses")
        print("4. Get Total Expenses")
        print("5. Change category and Expense Data for a User")
        print("6. Delete User and Data")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            user, category = add_user_category()
            is_user_category_added = True
        elif choice == "2":
            if not is_user_category_added:
                print("Please add user and category first.")
                continue

            amount = float(input("Enter expense amount: "))

            expense_data = {'amount': amount}
            add_expense(expense_data, category, user)
            print("Expense added successfully.")
        elif choice == "3":
            view_all_expenses()
        elif choice == "4":
            get_total_expenses()
        elif choice == "5":
            if not is_user_category_added:
                print("Please add user and category first.")
                continue

            available_usernames = [user.username for user in User.select()]
            if not available_usernames:
                print("No users.")
                continue

            print("Available usernames:")
            for username in available_usernames:
                print(username)

            selected_username = input("Enter username to modify: ")
            if selected_username not in available_usernames:
                print(f"User '{selected_username}' does not exist.")
                continue

            category_name = input("Enter new category name: ")
            try:
                new_category, created = Category.get_or_create(name=category_name)
            except Category.DoesNotExist:
                print(f"Category '{category_name}' does not exist.")
                continue

            amount = float(input("Enter expense amount: "))

            selected_user = User.get(User.username == selected_username)
            expense = Expense.select().where(Expense.user == selected_user).first()
            if expense:
                expense.category = new_category
                expense.amount = amount
                expense.save()
                print(f"Category and expense data updated for user '{selected_user.username}'.")
            else:
                print(f"User '{selected_user.username}' has no expenses.")
        elif choice == "6":
            available_usernames = [user.username for user in User.select()]
            if not available_usernames:
                print("No users found.")
                continue

            print("Available usernames:")
            for username in available_usernames:
                print(username)

            selected_username = input("Enter username to delete: ")
            delete_user(selected_username)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    create_tables()
    main_menu()
