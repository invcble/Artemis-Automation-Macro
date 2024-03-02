from threading import Thread
import time

# Define a function for each print statement
def print_one():
    print(1)
    time.sleep(2)
    print("end")

def print_two():
    print(2)
    time.sleep(2)
    print("end")


def print_three():
    print(3)
    time.sleep(2)
    print("end")

# Create threads for each function
Thread(target=print_one).start()
Thread(target=print_two).start()
Thread(target=print_three).start()