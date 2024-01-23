def main():
    text = input("Greeting: ")
    greeting(text)

def greeting(i):
    i = i.strip().title()
    hello = i.find("Hello")
    h = i.find("H")
    if hello == 0:
        print("$0")
    elif h == 0:
        print("$20")
    else:
        print("$100")

main()
