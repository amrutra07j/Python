class User:

    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def run_deco(function):
    def wrap(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrap

def details_deco(func):
    def wrap(*args, **kwargs):
        print(f"{func.__name__}, {args}, {kwargs}")
        return func(args[0], args[1])
    return wrap

@details_deco
def sagar(hi, hello):
    return f"Saying {hi} to all to tell {hello}"

@run_deco
def start(user):
    print(f"Your blog is here {user.name}!")


new_user = User('Rajaratnam')
new_user.is_logged_in = True
start(new_user)
print(sagar('hello', 'hi'))