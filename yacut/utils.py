import random
import string

LENGTH_RANDOM_CUSMOM_ID = 6


def random_custom_id() -> str:
    symbols = string.ascii_letters + string.digits
    return ''.join(
        random.choice(symbols) for _ in range(LENGTH_RANDOM_CUSMOM_ID)
    )
