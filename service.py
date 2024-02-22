import random
from string import ascii_letters, digits


def generate_username() -> str:
    return f'user{random.randint(0, 1000000)}'

def generate_password(length=8) -> str:
    return ''.join(random.choices(ascii_letters + digits, k=length))

def generate_post_name() -> str:
    return f'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

def generate_post_content() -> str:
    return f'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'