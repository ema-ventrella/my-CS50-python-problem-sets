import validator_collection as vc


def main():
    print(checker(input("What's your email address? ")))


def checker(email):
    try:
        vc.email(email)
    except ValueError:
        return "Invalid"
    else:
        return "Valid"


if __name__ == "__main__":
    main()
