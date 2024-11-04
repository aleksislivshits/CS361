import datetime

class Budget:
    def __init__(self):
        self.categories = {}

    def add_category(self, name, balance=0):
        self.categories[name] = balance

    def deposit(self, category, amount):
        if category in self.categories:
            self.categories[category] += amount
        else:
            print("Category not found.")

    def withdraw(self, category, amount):
        if category in self.categories:
            if self.categories[category] >= amount:
                self.categories[category] -= amount
            else:
                print("Insufficient funds.")
        else:
            print("Category not found.")

    def transfer(self, from_category, to_category, amount):
        if from_category in self.categories and to_category in self.categories:
            if self.categories[from_category] >= amount:
                self.categories[from_category] -= amount
                self.categories[to_category] += amount
            else:
                print("Insufficient funds.")
        else:
            print("Category not found.")

    def get_balance(self, category):
        if category in self.categories:
            return self.categories[category]
        else:
            print("Category not found.")

    def display_summary(self):
        print("Budget Summary:")
        for category, balance in self.categories.items():
            print(f"{category}: {balance}")

def main():
    my_budget = Budget()

    while True:
        print("\nBudget App Menu:")
        print("1. Add category")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Get balance")
        print("6. Display summary")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category_name = input("Enter category name: ")
            my_budget.add_category(category_name)
        elif choice == '2':
            category_name = input("Enter category name: ")
            amount = float(input("Enter deposit amount: "))
            my_budget.deposit(category_name, amount)
        elif choice == '3':
            category_name = input("Enter category name: ")
            amount = float(input("Enter withdrawal amount: "))
            my_budget.withdraw(category_name, amount)
        elif choice == '4':
            from_category = input("Enter source category: ")
            to_category = input("Enter destination category: ")
            amount = float(input("Enter transfer amount: "))
            my_budget.transfer(from_category, to_category, amount)
        elif choice == '5':
            category_name = input("Enter category name: ")
            balance = my_budget.get_balance(category_name)
            print(f"Balance in {category_name}: {balance}")
        elif choice == '6':
            my_budget.display_summary()
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()