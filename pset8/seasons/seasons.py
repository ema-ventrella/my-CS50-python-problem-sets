import sys
import inflect
from datetime import date
from datetime import datetime

p = inflect.engine()

def main():
    print(cal(str(input("Date of Birth: ")), date.today()))

def cal(birthday, today):
    try:
        birthday = datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        sys.exit("Invalid date")
    else:
        date_difference = today - birthday.date()
        count = int(date_difference.total_seconds() / 60)
        minutes = p.number_to_words(count, andword="").capitalize()
        return f"{minutes} minutes"

if __name__ == "__main__":
    main()
