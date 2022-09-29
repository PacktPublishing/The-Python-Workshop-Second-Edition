import time
import functools

def expensive_call():
    time.sleep(10)
def expensive_call2():
    time.sleep(20)


_constant_resolution = {
    "constants1": expensive_call,
    "constants2": expensive_call2,
}
@functools.lru_cache(maxsize=None)
def __getattr__(name):
    try:
        return _constant_resolution[name]()
    except KeyError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
