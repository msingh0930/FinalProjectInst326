import argparse

class BudgetManager:
    def __init__(self):
        """Initialize the BudgetManager object"""
        self.transactions = []
        self.income = 0

    def set_income(self, income):
        """Set the user's income"""
        self.income = income

    def transactionlist_add(self, category, amount):
        """This is the method that adds the transactions to the list of transactions
        Args:
            category(str): this is the category of the transactions i.e shopping or transportation
            amount(float): this is the amount of money that was spent in the transaction
        """
        self.transactions.append((category, amount))

    def calculate_insights(self):
        """Calculate insights based on transactions and income"""
        total = {}
        total_amount_spent = 0
        for category, amount in self.transactions:
            if category in total:
                total[category] += amount
            else:
                total[category] = amount
            total_amount_spent += amount

        # Calculate percentages for each category
        category_percentages = {}
        for category, amount in total.items():
            category_percentages[category] = (amount / self.income) * 100

        # Provide budgeting suggestions
        suggestions = []
        for category, percentage in category_percentages.items():
            if percentage > 30:
                suggestions.append(f"You should consider reducing spending on {category}.")

        return total_amount_spent, total, category_percentages, suggestions

    def display_insights(self):
        """Display insights based on transactions and income"""
        total_amount_spent, total, category_percentages, suggestions = self.calculate_insights()

        print(f"Total amount spent: ${total_amount_spent:.2f}")
        print("Category Spending:")
        for category, amount in total.items():
            percentage = category_percentages[category]
            print(f"{category}: ${amount:.2f} ({percentage:.2f}%)")

        print("\nBudgeting suggestions:")
        if not suggestions:
            print("Your spending looks balanced.")
        else:
            for suggestion in suggestions:
                print(suggestion)
                
        leftover_income = self.income - total_amount_spent
        print(f"\nAdded to savings: ${leftover_income:.2f}")

    def add_transactions(self):
        """Prompt the user to add transactions"""
        while True:
            category = input("Enter a category or type 'q' to see budget: ")
            if category.lower() == 'q':
                break
            try:
                amount = float(input(f"Enter the amount for {category}: "))
                self.transactionlist_add(category, amount)
            except ValueError:
                print("Invalid amount. Please try again.")

def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description="Budget Manager")
    parser.add_argument("income", type=float, help="Set monthly income")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    budget_manager = BudgetManager()
    budget_manager.set_income(args.income)
    budget_manager.add_transactions()
    budget_manager.display_insights()