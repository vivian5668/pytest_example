
def add(a, b):
    if not a.isdigit() or not b.isdigit():
        raise ValueError("Not a number")
    return a + b

def minus(a, b):
    return a - b