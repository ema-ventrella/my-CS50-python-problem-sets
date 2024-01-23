import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if re.search(r"^(\d{1,3}\.){3}\d{1,3}$", ip):
        for e in ip.split("."):
            if int(e) > 255:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()