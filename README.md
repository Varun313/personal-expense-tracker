# Personal Expense Tracker

A Python-based personal finance application designed to help users manage income, expenses, transactions, and financial insights through a simple command-line interface.

## Overview

Personal Expense Tracker allows users to record and manage their daily financial transactions in one place.

The application stores transaction data locally using JSON and provides tools for searching, filtering, editing, deleting, and analyzing financial records.

## Screenshots

### Main Menu

![Main Menu](screenshots/main-menu.png)

### Add Expenses

![Add Expenses](screenshots/expenses-menu.png)

### Financial Summary

![Financial Summary](screenshots/financial-summary.png)

### Monthly Analytics

![Monthly Analytics](screenshots/monthly-analytics.png)

### Category Analytics

![Category Analytics](screenshots/transaction-summary.png)

## Features

- Add income
- Add expenses
- View all transactions
- Search transactions
- Filter transactions
- Filter transactions by date
- View financial summary
- View monthly analytics
- View category analytics
- Edit transactions
- Delete transactions
- Validate user input
- Store transaction data using JSON

## Financial Summary

The application calculates:

- Total income
- Total expenses
- Current balance

The balance is calculated based on total income and total expenses.

## Analytics

The application provides basic financial insights including:

- Monthly transaction analysis
- Category-based expense analysis
- Income and expense comparison
- Overall financial balance

## Technology Stack

- Python
- JSON
- Git
- GitHub
- VS Code

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
├── ui/
│   ├── analytics.py
│   ├── dashboard.py
│   └── transactions.py
│
└── utils/
    ├── calculations.py
    ├── storage.py
    └── validators.py