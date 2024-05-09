import unittest
from FinalProject import BudgetManager

class TestBudgetManager(unittest.TestCase):
    def setUp(self):
        self.FinalProject = BudgetManager()
        self.FinalProject.set_income(5000)

    def test_set_income(self):
        self.assertEqual(self.FinalProject.income, 5000)

    def test_transactionlist_add(self):
        self.FinalProject.transactionlist_add("Groceries", 200)
        self.FinalProject.transactionlist_add("Dining", 100)
        self.assertListEqual(self.FinalProject.transactions, [("Groceries", 200), ("Dining", 100)])

    def test_calculate_insights(self):
        self.FinalProject.transactionlist_add("Groceries", 500)
        self.FinalProject.transactionlist_add("Rent", 2000)
        self.FinalProject.transactionlist_add("Entertainment", 300)

        total_amount_spent, total, category_percentages, suggestions = self.FinalProject.calculate_insights()

        self.assertEqual(total_amount_spent, 2800)
        self.assertDictEqual(total, {"Groceries": 500, "Rent": 2000, "Entertainment": 300})
        self.assertDictEqual(category_percentages, {"Groceries": 10.0, "Rent": 40.0, "Entertainment": 6.0})
        self.assertListEqual(suggestions, ["You should consider reducing spending on Rent."])



if __name__ == '__main__':
    unittest.main()