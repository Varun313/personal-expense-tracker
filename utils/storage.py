import json
from pathlib import Path


# Find the main project folder
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# Point to the data folder
DATA_FOLDER = PROJECT_FOLDER / "data"

# Point to the JSON file
DATA_FILE = DATA_FOLDER / "expenses.json"


def load_transactions():
    # Make sure the data folder exists
    DATA_FOLDER.mkdir(exist_ok=True)

    # If the file doesn't exist, return an empty list
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_transactions(transactions):
    # Make sure the data folder exists
    DATA_FOLDER.mkdir(exist_ok=True)

    # Save transactions to JSON
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=4)