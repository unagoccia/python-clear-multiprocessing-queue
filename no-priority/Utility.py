import string
import random
import time

def random_str(len):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(len)])

def random_sleep():
    time.sleep(random.randint(1, 5))
