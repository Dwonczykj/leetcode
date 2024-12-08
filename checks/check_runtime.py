import time
from functools import wraps

def runtime_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"Runtime: {runtime:.6f} seconds")
        return result
    return wrapper

def measure_runtime(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    runtime = end_time - start_time
    return result, runtime

def example_function(n):
    # Example function logic
    total = 0
    for i in range(n):
        total += i
    return total

# Measuring runtime
result, runtime = measure_runtime(example_function, 1000000)
print(f"Runtime: {runtime} seconds")