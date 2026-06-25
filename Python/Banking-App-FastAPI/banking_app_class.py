
import json
from pathlib import Path
import datetime


class bank_account:

    def __init__(self, owner, password, email, balance, credit_score, iban):
        self.owner = owner
        self.password = password
        self.email = email
        self.balance = balance
        self.credit_score = credit_score
        self.iban = iban
        # self.DOB = DOB

    def to_dict(self):

        return {
            "owner": self.owner,
            "email": self.email,
            "balance": self.balance,
            "credit_score": self.credit_score,
            "iban": self.iban

        }

    def check_balance(self):
        print(self.balance)
        return self.balance


class account_finances:
    def __init__(self, balance, action_type, transaction_id, account_id):
        self.balance = balance
        self.action_type = action_type
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.transactions = []

    def action(self, action_type, amount):
        now = datetime.datetime.now()
        if action_type == "withdraw":
            if self.balance - amount >= 0:
                self.balance = self.balance - amount
                self.transactions.append(
                    {"type": "withdraw", "amount": amount, "timestamp": now})
                print(
                    f"You have successfuly withdrawed {amount} from your account you have {self.balance} left in your account.")
            else:
                print("You cannot go in the negatives")

        elif action_type == "deposit":
            self.balance = amount + self.balance
            self.transactions.append({"type": "deposit", "amount": amount})
            print(
                f"You have successfuly deposited {amount} into your account you currently have {self.balance} left.")


    def show_transactions(self):
        print(self.transactions)
        return (self.transactions)

    def to_dict(self):

        return {
            "transactions": self.transactions
        }
