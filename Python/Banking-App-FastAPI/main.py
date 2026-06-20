from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from banking_app_class import bank_account

app = FastAPI()


class AccountCreate(BaseModel):
    owner: str
    balance: float
    credit_score: int


accounts_db = []


@app.get("/")
def root():
    return {"Hello": "World"}


global_ID_POOL = 0


def generate_id():
    global global_ID_POOL
    global_ID_POOL += 1
    return global_ID_POOL


@app.post("/account")
def create_account(account_data: AccountCreate):
    new_acc = bank_account(
        owner=account_data.owner,
        balance=account_data.balance,
        credit_score=account_data.credit_score,
        id=generate_id()
    )

    accounts_db.append(new_acc)
    return {"message": f"Account created for {new_acc.owner}"}


@app.get("/account/{account_id}")
def get_account(account_id: int):
    for account in accounts_db:
        if account.id == account_id:
            return account.to_dict()


@app.get("/accounts")
def list_accounts(limit: int = 10):

    return accounts_db[0:limit]
