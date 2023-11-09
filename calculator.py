def add(a, b):
    return a + b;

def sub(a, b):
    return a - b;

def mul(a, b):
    return a * b;

def div(a, b):
    if (b == 0):
        print("No");
    else:
        return a / b;

def main():
    print(add(1, 2));
    print(div(1, 0));
    
    return 0;

main();
