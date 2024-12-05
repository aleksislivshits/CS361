# Aleksis Livshits
# CS361: Software Engineering I
# Final Portfolio Project


import json
import os
import requests

users = {}


def save_budget_data(budget_data, filename='budget_data.json'):
    with open(filename, 'w') as file:
        json.dump(budget_data, file, indent=4)
    print("Budget saved successfully!")


def load_budget_file(filename='budget_data.json'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return json.load(file)


def register(email, password):
    """Register a new user with an email and password."""
    if email in users:
        print("Email already registered.")
    else:
        users[email] = password
        print("Registration successful.")


def login(email, password):
    """Log in an existing user."""
    if email in users and users[email] == password:
        print("Login successful.")
        print("WARNING: We will never share or sell your data or information to other companies. This software and its "
              "features will always be free to use!")  # I.H. 3
        return True
    else:
        print("Invalid email or password.")
        return False


class Motivation:
    """Class to manage motivational quotes and images."""
    def __init__(self):
        self.motivations = []

    def add_quote(self, quote):
        """Add a motivational quote."""
        self.motivations.append({'type': 'quote', 'content': quote})

    def add_image(self, image_path):
        """Add a motivational image."""
        self.motivations.append({'type': 'image', 'content': image_path})

    def display_motivations(self):
        """Display all motivational quotes and images."""
        print("Motivational Content:")
        for motivation in self.motivations:
            if motivation['type'] == 'quote':
                print(f"Quote: {motivation['content']}")
            elif motivation['type'] == 'image':
                print(f"Image: {motivation['content']}")

    def delete_motivation(self, index):
        """Delete a motivational entry by index."""
        if 0 <= index < len(self.motivations):
            del self.motivations[index]
            print("Motivation deleted successfully.")
        else:
            print("Invalid index.")


class Budget:
    """Class to manage budgeting categories and operations."""
    def __init__(self):
        self.categories = {}

    def add_category(name, amount):
        """Add a new budgeting category with a color."""
        budget_data = load_budget_file()
        category = {"name": name, "amount": amount}
        budget_data.update(category)
        save_budget_data(budget_data)
        print(f"Category '{name}' with amount {amount} added.")


    def delete_category(self, category_name):
        """Delete a category by name."""
        if category_name in self.categories:
            del self.categories[category_name]
            print(f"Category '{category_name}' deleted successfully.")
        else:
            print("Category not found.")

    def display_summary(self):
        """Display a summary of all budgeting categories and their balances."""
        budget_data = load_budget_file()
        if not budget_data:
            print("No budget data found!")
        else:
            print("\nYour Budget is: ")
            for category in budget_data:
                print(f"{category['name']}: ${category['amount']}")
        # print("Budget Summary:")
        # for category, details in self.categories.items():
        #     print(f"{category}: {details['balance']} (Color: {details['color']})")

    def deposit(self, category, amount):
        """Deposit an amount into a specified category."""
        if category in self.categories:
            self.categories[category] += amount
        else:
            print("Category not found.")

    def withdraw(self, category, amount):
        """Withdraw an amount from a specified category."""
        if category in self.categories:
            if self.categories[category] >= amount:
                self.categories[category] -= amount
            else:
                print("Insufficient funds.")
        else:
            print("Category not found.")

    def transfer(self, from_category, to_category, amount):
        """Transfer an amount from one category to another."""
        if from_category in self.categories and to_category in self.categories:
            if self.categories[from_category] >= amount:
                self.categories[from_category] -= amount
                self.categories[to_category] += amount
            else:
                print("Insufficient funds.")
        else:
            print("Category not found.")

    def get_balance(self, category):
        """Get the balance of a specified category."""
        if category in self.categories:
            return self.categories[category]
        else:
            print("Category not found.")

    def display_summary(self):
        """Display a summary of all budgeting categories and their balances."""
        print("Budget Summary:")
        for category, balance in self.categories.items():
            print(f"{category}: {balance}")

    def set_reminder_time(self):
        reminder_time = input("Enter your preferred reminder time (HH:MM format, 12-hour): ")

        response = requests.post('http://127.0.0.1:5003/set-reminder-time', json={"reminder_time": reminder_time})
        if response.status_code == 200:
            print(f"Reminder time set to {reminder_time}.")
        else:
            print("Failed to set your reminder time. Make sure that you entered your time in the format HH:MM.")

    def daily_reminder(self):
        response = requests.get('http://127.0.0.1:5003/daily-reminder')
        if response.status_code == 200:
            reminder_data = response.json()
            print(reminder_data['reminder'])

    def display_budgeting_resources(self):
        """Display links to external budgeting resources."""
        print("How to Budget Resources:")
        print("1. [Making a Budget](https://consumer.gov/managing-your-money/making-budget)")
        print("2. [Creating a Budget](https://bettermoneyhabits.bankofamerica.com/en/saving-budgeting/creating-a-budget"
              ")")
        print("3. [How to Make a Budget](https://www.ramseysolutions.com/budgeting/how-to-make-a-budget?srsltid=AfmBOor"
              "2FhAPN4hwEjxekqKu8Pd19q2w_aTyMFPFU7P0GD9naFr-UDnR)")


class SavingsGoal:
    def __init__(self, goal_amount):
        self.goal_amount = goal_amount
        self.current_savings = 0

    def add_savings(self, amount):
        self.current_savings += amount
        print(f"Current savings: ${self.current_savings:.2f}")

    def savings_progress(self):
        progress_percentage = (self.current_savings / self.goal_amount) * 100
        return progress_percentage

    def display_progress_bar(self):
        progress_percentage = self.savings_progress()
        bar_length = 50  # Length of the progress bar
        filled_length = int(bar_length * progress_percentage // 100)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f"Progress: |{bar}| {progress_percentage:.2f}% of your goal achieved.")

class BudgetingApp:
    def __init__(self):
        self.savings_goal = None

    def set_savings_goal(self):
        goal_amount = float(input("Enter your savings goal amount: $"))
        self.savings_goal = SavingsGoal(goal_amount)

    def input_savings(self):
        if self.savings_goal is None:
            print("Please set your savings goal first.")
            return
        amount = float(input("Enter the amount you want to add to your savings: $"))
        self.savings_goal.add_savings(amount)
        self.savings_goal.display_progress_bar()


# In the main function, update the call to add_category
def main(self=None):
    """Main function to run the user login and budgeting system."""
    motivation = Motivation()  # Initialize the Motivation class
    budget = Budget()
    budgeting_app = BudgetingApp()
    budget = load_budget_file()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit Application")
        choice = input("Choose an option: ")

        if choice == '1':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            register(email, password)
        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if login(email, password):
                my_budget = Budget()
                while True:
                    print("\nBudget App Menu:")
                    print("1. Add budgeting category")
                    print("2. Edit category")
                    print("3. Delete category")
                    print("4. Add expenses, debt, etc.")
                    print("5. Withdraw expenses")
                    print("6. Transfer expenses")
                    print("7. Get balance")
                    print("8. Display summary")
                    print("9. Motivation")
                    print("10. How to Budget") # I.H. 1
                    print("11. Logout")
                    print("12. BONUS: Set Savings Goal")
                    print("13. BONUS: Set Reminder Time")
                    print("14. BONUS: View Daily Reminder")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        name = input("Enter category name: ")
                        amount = float(input("Enter amount: $"))
                        Budget.add_category(name, amount)

                    elif choice == '2':
                        old_name = input("Enter the current category name: ")
                        new_name = input("Enter the new category name: ")
                        new_color = input("Enter the new font color: ")
                        my_budget.edit_category(old_name, new_name, new_color)  # Call the edit method
                    elif choice == '3':
                        category_name = input("Enter the category name to delete: ")
                        my_budget.delete_category(category_name)
                        print(f"Your category {category_name} has been deleted!")

                    elif choice == '4':
                        budget['income'] = float(input("Enter your total income: "))
                        print("\nEnter your expenses (type 'done' when finished):")
                        expenses = []
                        while True:
                            category = input("Enter category name: ")
                            if category.lower() == 'done':
                                break
                            amount = float(input(f"Enter the amount for {category}:"))
                        budget['debt'] = float(input("Enter your current debt: "))
                        budget['expenses'] = expenses
                        save_budget_data(budget)
                        print("\nYour budget data has been successfully saved!")

                    elif choice == '5':
                        category_name = input("Enter category name: ")
                        amount = float(input("Enter withdrawal amount: "))
                        my_budget.withdraw(category_name, amount)
                    elif choice == '6':
                        from_category = input("Enter source category: ")
                        to_category = input("Enter destination category: ")
                        amount = float(input("Enter transfer amount: "))
                        my_budget.transfer(from_category, to_category, amount)
                    elif choice == '7':
                        category_name = input("Enter category name: ")
                        balance = my_budget.get_balance(category_name)
                        print(f"Balance in {category_name}: {balance}")
                    elif choice == '8':
                        my_budget.display_summary()
                    elif choice == '9':
                        print("\nMotivation Menu:")
                        print("1. Add Quote")
                        print("2. Add Image")
                        print("3. View Motivations")
                        print("4. Delete Motivation")
                        print("5. Logout")
                        motivation_choice = input("Choose an option: ")

                        if motivation_choice == '1':
                            quote = input("Enter your motivational quote: ")
                            motivation.add_quote(quote)
                        elif motivation_choice == '2':
                            image_path = input("Enter the path of your motivational image: ")
                            motivation.add_image(image_path)
                        elif motivation_choice == '3':
                            motivation.display_motivations()
                        elif motivation_choice == '4':
                            index = int(input("Enter the index of the motivation to delete: "))
                            motivation.delete_motivation(index)
                        elif motivation_choice == '5':
                            break
                        else:
                            print("Invalid choice.")
                    elif choice == '10':
                        my_budget.display_budgeting_resources() # Calling the method here
                    elif choice == '11':
                        break
                    elif choice == '12':
                        budget['goal'] = float(input("Enter your budget goal: "))
                        save_budget_data(budget)
                    elif choice == '13':
                        Budget.set_reminder_time(self)
                    elif choice == '14':
                        Budget.daily_reminder(self)
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
