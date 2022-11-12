import string
from random import sample

def get_random_password() -> str:
    lenght_ = 8
    allowed_symbols = string.ascii_letters + string.digits
    password = "".join(sample(allowed_symbols, lenght_))
    return password


print(get_random_password())
