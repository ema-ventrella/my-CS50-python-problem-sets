def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer_check(answer)

def answer_check(i):
    i = i.strip().title()
    if i == "42" or i == "Forty-Two" or i == "Forty Two":
        print("Yes")
    else:
        print("No")
    return i

main()
