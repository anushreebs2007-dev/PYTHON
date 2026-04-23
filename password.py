import string
import random

def generate_password(length=16):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    password = [random.choice(upper)]
    password.append(random.choice(lower))
    password.append(random.choice(digits))
    password.append(random.choice(special))
    all_chars = upper + lower + digits + special
    while len(password) < length:
        password.append(random.choice(all_chars))
    rest = password[1:]
    random.shuffle(rest)
    password = [password[0]] + rest
    return "".join(password)
try:
    print("Generated Password:", generate_password(16))
except ValueError as e:
    print("Exception:", e)
 