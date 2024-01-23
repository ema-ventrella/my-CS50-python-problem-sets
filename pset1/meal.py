def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    time_time = hours + minutes / 60.0
    return time_time

def main():
    time_hours = input("What time is it? ")
    time_time = convert(time_hours)
    if 7.0 <= time_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_time <= 13.0:
        print("lunch time")
    elif 18.0 <= time_time <= 19.0:
        print("dinner time")

if __name__ == "__main__":
    main()
