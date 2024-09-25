# Financial API

A comprehensive financial API built with Python, Django, and Django Rest Framework (DRF). This API allows users to manage financial transactions, retrieve user-specific transaction data, and generate financial reports.

## Features

- **Transaction Management**
  - List and create transactions.
  - Retrieve, update, and delete individual transactions.
  - Pagination and filtering options.

- **User Management**
  - Retrieve a list of registered users.
  - Get transactions for a specific user.

- **Reports**
  - Generate monthly or yearly summaries of transactions for a given user.

## Endpoints

### Transactions

- `GET /api/transactions/`: List all transactions.
- `POST /api/transactions/`: Create a new transaction.
- `GET /api/transactions/<transaction_id>/`: Retrieve a specific transaction.
- `PUT /api/transactions/<transaction_id>/`: Update a specific transaction.
- `DELETE /api/transactions/<transaction_id>/`: Delete a specific transaction.

### Users

- `GET /api/users/`: List all registered users.
- `GET /api/users/<user_id>/transactions/`: Retrieve transactions for a specific user.

### Reports

- `GET /api/reports/`: Generate financial reports for a user.

## Installation

### 1. Clone the Repository

Begin by cloning the repository to your local machine:
 
```bash
git clone https://github.com/Muhammad0074/Pet-Classification-Project.git
cd Pet-Classification-Project

```
### 2. open app.py terminal

- create virtual environment `pip install virtualenv venv`
- activate venv  `venv/Scripts/activate`
- install requirements  `pip install -r requirements.txt`
- run application  `python app.py`
