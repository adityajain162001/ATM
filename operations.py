from database import get_user, update_balance

def check_balance(account_number):
    user = get_user(account_number)
    if user:
        return user[2]
    return None

def withdraw(account_number, amount):
    user = get_user(account_number)
    if user and amount > 0 and user[2] >= amount:
        new_balance = user[2] - amount
        update_balance(account_number, new_balance)
        return new_balance
    return None

def deposit(account_number, amount):
    user = get_user(account_number)
    if user and amount > 0:
        new_balance = user[2] + amount
        update_balance(account_number, new_balance)
        return new_balance
    return None
