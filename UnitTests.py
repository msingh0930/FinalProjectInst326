import unittest
import sys
from FinalProject import BudgetManager, parse_args
#Unit tests that test each method in our code
class TestBudgetManager(unittest.TestCase):
    def setUp(self):
        sys.argv = ['test_script']
        self.budget_manager = BudgetManager()
        self.budget_manager.set_income(5000)

    
    def test_set_income(self):
        self.assertEqual(self.budget_manager.income, 5000)

    
    def test_transactionlist_add(self):
        self.budget_manager.transactionlist_add("Groceries", 200)
        self.budget_manager.transactionlist_add("Dining", 100)
        self.assertListEqual(self.budget_manager.transactions, [("Groceries", 200), ("Dining", 100)])

    
    def test_calculate_insights(self):
        self.budget_manager.transactionlist_add("Groceries", 500)
        self.budget_manager.transactionlist_add("Rent", 2000)
        self.budget_manager.transactionlist_add("Entertainment", 300)
        total_amount_spent, total, category_percentages, suggestions = self.budget_manager.calculate_insights()
        self.assertEqual(total_amount_spent, 2800)
        self.assertDictEqual(total, {"Groceries": 500, "Rent": 2000, "Entertainment": 300})
        self.assertDictEqual(category_percentages, {"Groceries": 10.0, "Rent": 40.0, "Entertainment": 6.0})
        self.assertListEqual(suggestions, ["You should consider reducing spending on Rent."])

    
    def test_command_line_args(self):
        sys.argv = ['test_script', '4500']
        args = parse_args()
        self.assertEqual(args.income, 4500)

if __name__ == '__main__':
    unittest.main()
