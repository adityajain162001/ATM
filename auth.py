from database import get_user

# Function to authenticate user
def authenticate(account_number, pin):
    user = get_user(account_number)
    if user and user[1] == pin:
        return user
    return None
