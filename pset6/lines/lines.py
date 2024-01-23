import sys


def main():
    nlines = 0
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")
    else:
        try:
            file = open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File doesn't exist.")
        else:
            for line in file:
                if not line.lstrip().startswith("#") and line.lstrip() != "":
                    nlines += 1
            print(nlines)
            file.close()

main()
