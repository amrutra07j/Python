import time


def setter(finder):
    time.sleep(1)
    return finder

# hi = deco_find()
@setter
def oho():
    print("ra")
oho()

print(time.time())