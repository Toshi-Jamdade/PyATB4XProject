import functools
import time

def time_decorator(func):
    def wrapper_fun():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"Time taken by function {end_time - start_time}")
    return wrapper_fun()

@time_decorator
def test_ui_1():
    print("Add a function, time taken by this function")
    time.sleep(2)       # means wait for 2 seconds

@time_decorator
def test_ui_2():
    print("Add a function, time taken by this function")
    time.sleep(5)       ## means wait for 5 seconds

# 1726410381.725668
# Add a function, time taken by this function
# 1726410383.726866
# Time taken by function 2.0011980533599854
# 1726410469.8941495
# Add a function, time taken by this function
# 1726410474.8944523
# Time taken by function 5.000302791595459


# 1726410381.725668 - This is in Epoch time format

# Types of decorators:
# @staticmethod
# @classmethod
# @property
# @functools.wraps
# This we will use them in OOPs

# Chaining Decorators - means adding multiple decorators to the same function
