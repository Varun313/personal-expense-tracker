# Personal Expense Tracker

A Python-based personal finance application for tracking income,
expenses, transactions, and financial balance.

## Project Status

Active development. The core expense tracking and analytics features are currently implemented.

## Current Features

- Add income
- Add expenses
- View all transactions
- Search transactions
- Filter transactions by category
- Filter transactions by type
- Filter transactions by date
- Monthly analytics
- Category-wise spending analytics
- Calculate total income
- Calculate total expenses
- Calculate balance
- Edit transactions
- Delete transactions
- Save transaction data using JSON
- Input validation

## Technology

- Python
- JSON
- Git
- GitHub

## Project Structure

```text
Personal Expense Tracker
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── expenses.json
│
├── utils/
│   ├── calculations.py
│   ├── storage.py
│   └── validators.py
│
└── ui/
    ├── dashboard.py
    ├── transactions.py
    └── analytics.py