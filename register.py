import re

def register(email, password):
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        raise ValueError('Invalid email')
    if len(password) < 8:
        raise ValueError('Password must be at least 8 characters')
    return {'email': email, 'status': 'registered'}
