def main():
    values = input("Expression: ")
    values = values.split()
    x, y, z = values[0], values[1], values[2]
    calculator(x, y, z)

def calculator(a, b, c):
    a = float(a)
    c = float(c)
    if b == "+":
        print(a + c)
    elif b == "-":
        print(a - c)
    elif b == "*":
        print(a * c)
    elif b == "/":
        print(a / c)

main()
