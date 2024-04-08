class BudgetManager:
    def __init__(self):
        """Initialize the BudgetManager object"""
        #this is the list to store the transactions in this format (category, amount)
        self.transactions = []

    def transactionlist_add(self, category, amount):
        """This is the method that adds the transactions to the list of transactions
        
        Args: category(str): this is the category of the transactions i.e shopping or transportation
              amount(float): this is the amount og money that was spent in the transaction"""
        self.transactions.append((category, amount))

    def calculate_insights(self):
        """This is what calculates the insights based on the transactions made
        
        Returns: a tuple that contains the total spent which is a float and a dictionary of category-wise spending which is in format (string, float)"""
        #this is the dictionary for the total spending for each category
        totals =  {}
        #this is the toal amount spent throughout all the categories
        total_amount_spend = 0

        for category, amount in self.transactions:
            #this is what updates the category totals and the total amount spent overall
            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount
            total_amount_spend += amount
        return total_amount_spend, totals
