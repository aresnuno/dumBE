import random
import time

def generate_unique_filename():
    return str(int(time.time()))  # Or use: return str(random.randint(100000, 999999))
