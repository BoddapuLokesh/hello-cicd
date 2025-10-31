def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        print("Division by zero, Invalid Input")
    return a/b

if __name__ == "__main__":
    print(add(2,3))
    print(subtract(4,2))
    print(multiply(7,2))
    print(divide(12,6))