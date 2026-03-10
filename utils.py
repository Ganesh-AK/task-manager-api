import time
import functools

def timer(func):
    @functools.wraps(func)       # copies original function's name
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)   # call the real function
        end = time.time()
        print(f"⏱  {func.__name__} took {(end-start)*1000:.1f}ms")
        return result
    return wrapper

def validate_priority(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        priority = kwargs.get('priority', 'medium')
        if priority not in ['low', 'medium', 'high']:
            print(f"❌ Invalid priority '{priority}'. Use: low, medium, high")
            return
        return func(*args, **kwargs)
    return wrapper