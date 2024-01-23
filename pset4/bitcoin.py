import sys
import requests


def main():
    try:
        n = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        file_data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = file_data.json()
        usd = data["bpi"]["USD"]["rate"].replace(",", "").replace(".", ".")
        ammount = float(usd) * n
        print(f"${ammount:,.4f}")


main()
