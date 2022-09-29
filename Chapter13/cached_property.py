class MyClass:
    @functools.cached_property
    def myvar(self):
        return expensive_operation()
