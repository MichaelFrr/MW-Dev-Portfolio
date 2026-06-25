import datetime
from bank_db import execute_write_query, execute_read_query
from faker import Faker
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import bcrypt
from banking_app_class import bank_account


app = FastAPI()
fake = Faker()
now = datetime.datetime.now()


class AccountCreate(BaseModel):
    owner: str
    password: str
    email: str
    # unused for now DOB: str


class AccountOut(BaseModel):
    account_id: int
    owner: str

    class Config:
        orm_mode = True


logs = []
accounts_db = []


@app.get("/")
def root():
    return {"Hello": "World"}


def generate_iban():
    iban = fake.iban()
    return iban


@app.post("/account")
def create_account(account_data: AccountCreate):
    new_acc = bank_account(
        owner=account_data.owner,
        email=account_data.email,
        password=bcrypt.hashpw(account_data.password.encode(
            'utf-8'), bcrypt.gensalt()).decode('utf-8'),
        balance=0.0,
        credit_score=600,
        iban=generate_iban()
    )
    read_query = '''SELECT * FROM "user" WHERE email = %s '''
    acc_email = account_data.email

    email_mem = []
    email_mem.append(acc_email)
    result = execute_read_query(read_query, email_mem, "fetch_row", 2)
    for email in email_mem:
        print(result)
        print(email)
        if email == result:
            raise HTTPException(status_code=400, detail="Email already exists")

    insert_query = ''' insert into "user" (owner, email, password) values(%s,%s,%s)'''
    execute_write_query(insert_query, (new_acc.owner,
                                       new_acc.email, new_acc.password))

    logs.append(
        f"account has been created. data:{new_acc.owner, new_acc.email}, timestamp: {now}")

    return {"message": f"Account created for {new_acc.owner}, {logs}"}


@app.get("/account/{account_id}")
def get_account(account_id: int):
    read_query = '''SELECT * FROM "user" WHERE ID = %s '''
    acc_idstr = str(account_id)
    result = execute_read_query(read_query, acc_idstr, "fetch_one")
    if result:
        return result

    raise HTTPException(
        status_code=404, detail=f"the account with the user id {account_id} has not been found")


@app.get("/accounts")
def list_accounts(limit: int = 10):

    read_query = '''SELECT * FROM "user" LIMIT %s '''
    result = execute_read_query(read_query, (limit,))
    return result


@app.get("/logs")
def get_logs(limit: int = 10):
    return logs[0:limit]
