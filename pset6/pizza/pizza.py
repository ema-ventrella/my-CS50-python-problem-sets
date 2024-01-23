import sys
import csv
from tabulate import tabulate


def main():
    if sys.argv[1].endswith(".csv") and len(sys.argv) == 2:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                print(tabulate(reader, headers="keys", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File doesn't exist.")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


main()
