import string
import random


alphabet = string.ascii_letters + string.digits + string.punctuation


def rstr(num: int = 0, fix: bool = False):
    num = int(num) or 8
    num = num if num > 8 else 8
    if fix:
        random.seed(num)
    result = ''
    for i in range(num):
        rand = random.randint(0, len(alphabet) - 1)
        result += alphabet[rand]
    return result