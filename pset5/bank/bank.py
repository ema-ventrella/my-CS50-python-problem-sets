def main():
    text = str(input("Greeting: "))
    money = value(text)
    print(f"${money}")

def value(greeting):
    greeting = greeting.strip().title()
    hello = greeting.find("Hello")
    h = greeting.find("H")
    if hello == 0:
        return 0
    elif h == 0:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()