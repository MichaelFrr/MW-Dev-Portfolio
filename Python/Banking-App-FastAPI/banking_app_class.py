
import json
from pathlib import Path
import datetime
now = datetime.datetime.now()


class bank_account:

    def __init__(self, owner, balance, credit_score, id):
        self.owner = owner
        self.balance = balance
        self.credit_score = credit_score
        self.transactions = []
        self.id = id

    def to_dict(self):

        return {
            "owner": self.owner,
            "balance": self.balance,
            "credit_score": self.credit_score,
            "transactions": self.transactions
        }

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            self.transactions.append({"type": "withdraw", "amount": amount})
            print(
                f"You have successfuly withdrawed {amount} from your account you have {self.balance} left in your account.")
        else:
            print("You cannot Go in the negatives")

    def deposit(self, amount):
        self.balance = amount + self.balance
        self.transactions.append({"type": "deposit", "amount": amount})
        print(
            f"You have successfuly deposited {amount} into your account you currently have {self.balance} left.")

    def check_balance(self):
        print(self.balance)
        return self.balance

    def show_transactions(self):
        print(self.transactions)
        return (self.transactions)

    def save(self):
        data = {
            "owner": self.owner,
            "balance": self.balance,
            "credit_score": self.credit_score,
            "transactions": self.transactions,
            "Date": now.isoformat()
        }

        with open(f"{self.owner}_account.json", "w") as file:
            json.dump(data, file, indent=4)

    def load(self, owner):
        filepath = Path(f"{self.owner}_account.json")
        if not filepath.exists():
            print(f"No saved data found for {self.owner}. Starting fresh.")
            return
        with open(f"{owner}_account.json", "r") as file:
            data = json.load(file)
        self.owner = data["owner"]
        self.balance = data["balance"]
        self.credit_score = data["credit_score"]
        self.transactions = data["transactions"]
