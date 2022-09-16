import time
def deco_delay(function):
    def wrap_func():
        time.sleep(2)
        function()
    return wrap_func

@deco_delay
def say_hi():
    print('jadrisas busdaris gosdavor')

say_hi()

hi = deco_delay(say_hi)
hi()