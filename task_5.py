import string
from random import sample

def get_random_password(lenght = 8) -> str:
    allowed_symbols = string.ascii_letters + string.digits
    password = "".join(sample(allowed_symbols, lenght))
    return password


print(get_random_password())
