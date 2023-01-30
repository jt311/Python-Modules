import time

def rand_func(num):
    print(f'First function sleeping for {num} second(s)')
    time.sleep(num)
    return f'Completed first function in {num} second(s)'

