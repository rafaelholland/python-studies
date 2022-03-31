friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0
    
    
"""
    Default values for parameters;
"""

accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balance"""
    accounts[name] += amount
    return accounts[name]

add_balance(500.00)
print(accounts['checking'])