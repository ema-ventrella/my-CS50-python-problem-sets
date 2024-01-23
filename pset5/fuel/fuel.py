def main():
    fraction = input("Fraction: ")
    result = gauge(convert(fraction))
    print(result)

def convert(fraction):
    x,y = fraction.split("/")
    try:
        return (int(x)/int(y)) * 100
    except (ValueError,ZeroDivisionError):
        raise

def gauge(percentage):
    if 0 <= percentage <= 100:
        if percentage >= 99:
            return "F"
        elif percentage <= 1:
            return "E"
        else:
            return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()