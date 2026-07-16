def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def main():
    print("Testing the calculator module")
    print(add(5, 3))
    print(subtract(10, 4))
    print(__name__)

if __name__ == "__main__":
    main()