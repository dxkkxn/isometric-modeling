import constants
def a():
    constants.a = 60
    print(f"from module 1 contstants.a = {constants.a}")

def b():
    print(f"from module 1 contstants.b = {constants.b}")
