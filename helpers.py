import random
import string


def random_char():
    return str(''.join(random.choice(string.ascii_letters) for x in range(6)))
