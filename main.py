
users = {}

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
              "features will always be free to use!") # I.H. 3
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

    def add_category(self):
        """Add a new budgeting category with a color."""
        name = input("Enter category name: ")
        color = input("Enter font color (red, green, blue, yellow, purple, pink): ")

        if color not in ['red', 'green', 'blue', 'yellow', 'purple', 'pink']:
            print("Invalid color. Defaulting to black.")
            color = 'black'

        self.categories[name] = {'balance': 0, 'color': color}
        print(f"Category '{name}' added with color '{color}'.")

    def change_color(self, category, new_color):
        """Change the color of a specified category."""
        if category in self.categories:
            if new_color in ['red', 'green', 'blue', 'yellow', 'purple', 'pink']:
                self.categories[category]['color'] = new_color
                print(f"Color for {category} changed to {new_color}.")
            else:
                print("Invalid color choice.")
        else:
            print("Category not found.")

    def edit_category(self, old_name, new_name, new_color):
        """Edit an existing category's name and color."""
        if old_name in self.categories:
            if new_color not in ['red', 'green', 'blue', 'yellow', 'purple', 'pink']:
                print("Invalid color. Defaulting to black.")
                new_color = 'black'
            self.categories[new_name] = self.categories.pop(old_name)
            self.categories[new_name]['color'] = new_color
            print(f"Category '{old_name}' updated to '{new_name}' with color '{new_color}'.")
        else:
            print("Category not found.")

    def delete_category(self, category_name):
        """Delete a category by name."""
        if category_name in self.categories:
            del self.categories[category_name]
            print(f"Category '{category_name}' deleted successfully.")
        else:
            print("Category not found.")

    def display_summary(self):
        """Display a summary of all budgeting categories and their balances."""
        print("Budget Summary:")
        for category, details in self.categories.items():
            print(f"{category}: {details['balance']} (Color: {details['color']})")

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

    def display_budgeting_resources(self):
        """Display links to external budgeting resources."""
        print("How to Budget Resources:")
        print("1. [Making a Budget](https://consumer.gov/managing-your-money/making-budget)")
        print("2. [Creating a Budget](https://bettermoneyhabits.bankofamerica.com/en/saving-budgeting/creating-a-budget"
              ")")
        print("3. [How to Make a Budget](https://www.ramseysolutions.com/budgeting/how-to-make-a-budget?srsltid=AfmBOor"
              "2FhAPN4hwEjxekqKu8Pd19q2w_aTyMFPFU7P0GD9naFr-UDnR)")

# In the main function, update the call to add_category
def main():
    """Main function to run the user login and budgeting system."""
    motivation = Motivation()  # Initialize the Motivation class
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
                    print("1. Add category")
                    print("2. Edit category")
                    print("3. Delete category")
                    print("4. Deposit")
                    print("5. Withdraw")
                    print("6. Transfer")
                    print("7. Get balance")
                    print("8. Display summary")
                    print("9. Motivation")
                    print("10. How to Budget") # I.H. 1
                    print("11. Logout")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        my_budget.add_category()  # Call the updated method

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
                        category_name = input("Enter category name: ")
                        amount = float(input("Enter deposit amount: "))
                        my_budget.deposit(category_name, amount)
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
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()