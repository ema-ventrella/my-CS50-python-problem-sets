def str_check(i):
    snakecase = ""
    for l in i:
        if l.isupper():
            snakecase += f"_{l.lower()}"
        else:
            snakecase += l
    return snakecase

def main():
    text = input("camelCase: ")
    snakecase = str_check(text)
    print(snakecase)

main()
