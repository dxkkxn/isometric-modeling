
class Test():
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

if __name__ == "__main__" :
    x = Test("aaaaaa", "bbbbbbbbbbbbb")
    print(x.__a, x.__b)
