from check_runtime import runtime_decorator
from check_memoryusage import custom_memory_decorator


@runtime_decorator
# @memory_decorator
@custom_memory_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Usage
result = example_function(1000000)