import sys
import csv


def main():
    names = []
    houses = []
    first = []
    last = []
    if len(sys.argv) == 3 and sys.argv[1].endswith(".csv"):
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    names.append(row["name"])
                    houses.append(row["house"])
                for name in names:
                    first.append(name.split(", ")[1])
                    last.append(name.split(", ")[0])
                with open(sys.argv[2], "w") as after_file:
                    writer = csv.DictWriter(
                        after_file, fieldnames=["first", "last", "house"]
                    )
                    writer.writerow({"first": "first", "last": "last", "house": "house"})
                    for i in range(len(first)):
                        writer.writerow(
                            {"first": first[i], "last": last[i], "house": houses[i]}
                        )
        except FileNotFoundError:
            sys.exit("File doesn't exist")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("File must be a .csv")


if __name__ == "__main__":
    main()