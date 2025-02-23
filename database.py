import sqlite3

# Initialize the database
def init_db():
    conn = sqlite3.connect("atm.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        account_number TEXT PRIMARY KEY,
                        pin TEXT NOT NULL,
                        balance REAL NOT NULL)''')
    conn.commit()
    conn.close()

# Function to fetch user data
def get_user(account_number):
    conn = sqlite3.connect("atm.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE account_number=?", (account_number,))
    user = cursor.fetchone()
    conn.close()
    return user

# Function to update balance
def update_balance(account_number, new_balance):
    conn = sqlite3.connect("atm.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance=? WHERE account_number=?", (new_balance, account_number))
    conn.commit()
    conn.close()

# Function to create a user (for testing purposes)
def create_user(account_number, pin, balance):
    if get_user(account_number):  # Check if user already exists
        print(f"User with account number {account_number} already exists.")
        return
    conn = sqlite3.connect("atm.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (account_number, pin, balance))
    conn.commit()
    conn.close()
    print(f"User {account_number} created successfully.")

