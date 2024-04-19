import random
import re
from string import ascii_letters, digits


def generator_password(k=10):
    password = random.choices(ascii_letters, k=k)
    password.extend(random.choices(digits, k=k))
    return ''.join(password)
