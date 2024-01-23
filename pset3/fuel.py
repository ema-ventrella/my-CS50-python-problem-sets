# Ask to the user the fraction, ecc..
def main():
    while True:
        fuel = input("Fraction: ")
        try:
            x, y = fuel.split('/')
            x, y = int(x), int(y)
            tank = calculate(x, y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            tank_full(tank)
            break

# Calculate the %
def calculate(x, y):
    tank = round(x / y * 100, 0)
    return int(tank)

# How full is the tank?
def tank_full(tank):
    if 99 <= tank <= 100:
        print("F")
    elif 1 < tank < 99:
        print(f"{tank}%")
    elif tank <= 1:
        print("E")
    elif tank > 100:
        main()

main()