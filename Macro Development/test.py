from threading import Thread
import time
from concurrent.futures import ThreadPoolExecutor as pool

# Define a function for each print statement
def print_one():
    print(1)
    time.sleep(2)
    print("end")

def print_two():
    print(2)
    time.sleep(2)
    raise Exception("lmao")


def print_three():
    print(3)
    time.sleep(2)
    print("end")

# Create threads for each function
# Thread(target=print_one).start()
# Thread(target=print_two).start()
# Thread(target=print_three).start()

# pool().submit(print_one)
# pool().submit(print_two)
# pool().submit(print_three) 
with pool() as p:
    print_two()

    # raise Exception