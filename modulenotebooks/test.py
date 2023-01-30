import time
import math

def rand_func(num):
    print(f'First function sleeping for {num} second(s)')
    time.sleep(num)
    return f'Completed first function in {num} second(s)'


def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

