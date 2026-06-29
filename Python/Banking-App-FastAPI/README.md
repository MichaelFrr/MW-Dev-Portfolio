# This is an object oriented programming banking api that is built to handle core financial transactions, user credit evaluation, and secure data persistence

## Features: 

* Account creation and logging in: You can create an account using a username and a password, and login to your account at any time.

* Credit evaluation and loan applications: Your credit score is evaluated and you can apply for a loan and if your credit score is high enough you can get accepted.

* Secure money managment actions such as Deposits and withdrawls: You can deposit and withdraw money from and to your account

* Secure money transfer to other accounts: You can transfer money from your account to another account by knowing the other account number



## Tech Stack:
* Backend Framework: `FastAPI (Asynchronous Python)`

* Database: `PostgreSQL`

* Data Validation & Serialization: `Pydantic / SQLModel`

* Security: `JWT (JSON Web Tokens) & Bcrypt (Password Hashing)`



  
### As an API designed with fintech principles in mind, security boundaries are enforced at the route level

* Passwords are never stored in plain text (hashed using bcrypt).
* Account isolation ensures authenticated users can only access or manipulate their own account IDs, preventing IDOR (Insecure Direct Object Reference) vulnerabilities.
* Anti Bot Security such as rate limiting to prevent brute forcing and DDOS attacks
* Anti Fraud protection
