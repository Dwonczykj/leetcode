# from memory_profiler import memory_usage
from functools import wraps
import tracemalloc # for workaround memory_decorator: custom_memory_decorator

# def memory_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         mem_usage = memory_usage((func, args, kwargs), interval=0.1)
#         print(f"Memory Usage: {max(mem_usage) - min(mem_usage):.6f} MiB")
#         return func(*args, **kwargs)
#     return wrapper
    
def custom_memory_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Current memory usage: {current / 10**6:.6f} MiB; Peak: {peak / 10**6:.6f} MiB")
        return result
    return wrapper
    
def example_function(n):
    # Example function logic
    total = 0
    for i in range(n):
        total += i
    return total

# # Measuring memory usage
# mem_usage = memory_usage((example_function, (1000000,)), interval=0.1)
# print(f"Memory Usage: {max(mem_usage) - min(mem_usage)} MiB")