menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = []
    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            break
        else:
            check(item, total)

def check(item, total):
    if item in menu:
        total.append(menu[item])
        print(f"Total: ${sum(total):.2f}")
    else:
        pass
            
main()