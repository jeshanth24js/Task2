import json

class Transaction:
    def __init__(self, category, amount, transaction_type):
        self.category = category
        self.amount = amount
        self.transaction_type = transaction_type

class BudgetTracker:
    def __init__(self, filename):
        self.transactions = []
        self.filename = filename

    def add_transaction(self, category, amount, transaction_type):
        transaction = Transaction(category, amount, transaction_type)
        self.transactions.append(transaction)

    def calculate_budget(self):
        income = sum(t.amount for t in self.transactions if t.transaction_type == 'income')
        expense = sum(t.amount for t in self.transactions if t.transaction_type == 'expense')
        return income - expense

    def analyze_expenses(self):
        categories = {}
        for t in self.transactions:
            if t.transaction_type == 'expense':
                if t.category not in categories:
                    categories[t.category] = 0
                categories[t.category] += t.amount
        return categories

    def save_transactions(self):
        with open(self.filename, 'w') as f:
            json.dump([t.__dict__ for t in self.transactions], f)

    def load_transactions(self):
        try:
            with open(self.filename, 'r') as f:
                self.transactions = [Transaction(**t) for t in json.load(f)]
        except FileNotFoundError:
            self.transactions = []

tracker = BudgetTracker('transactions.json')
tracker.load_transactions()
print(f"Remaining budget: {tracker.calculate_budget()}")
print(f"Expense analysis: {tracker.analyze_expenses()}")
