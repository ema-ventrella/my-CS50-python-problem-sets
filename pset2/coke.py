# Define how much needs to be paid

def main():
    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = ask()
        amount = amount - coin
        change(amount)

# Ask to the user how wants to pay: using only coins of 25, 10 or 5 cent

def ask():
    coin = int(input(f"Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        return coin
    else:
        coin = 0
        return coin

# Give the change

def change(c):
    if c <= 0:
        print(f"Change Owed: {c * -1}")

# Play

main()
