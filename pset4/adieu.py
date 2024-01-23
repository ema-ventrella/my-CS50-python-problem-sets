import inflect


def main():
    p = inflect.engine()
    mylist = []
    while True:
        try:
            user_input = str(input("Name: ")).strip()
            mylist.append(user_input)
        except EOFError:
            print(f"Adieu, adieu, to {p.join(mylist)}", end="\n")
            break

if __name__ == "__main__":
    main()