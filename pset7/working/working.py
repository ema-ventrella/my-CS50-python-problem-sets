import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = re.search(r"^([1-9][0-2]?)(:[0-5][0-9])? ([A-P]M)? to ([1-9][0-2]?)(:[0-5][0-9])? ([A-P]M)?", s, re.IGNORECASE)
    if time:
        groups = list(time.groups())
        if 0 < int(groups[0]) < 13 and 0 < int(groups[3]) < 13:
            
            if (groups[2] == "pm" and groups[0] != "12") or (groups[2] == "PM" and groups[0] != "12"):
                groups[0] = int(groups[0]) + 12
            if (groups[5] == "pm" and groups[3] != "12") or (groups[5] == "PM" and groups[3] != "12"):
                groups[3] = int(groups[3]) + 12
                
            if (groups[2] == "am" and groups[0] == "12") or (groups[2] == "AM" and groups[0] == "12"):
                groups[0] = "00"
            if (groups[5] == "am" and groups[3] == "12") or (groups[5] == "AM" and groups[3] == "12"):
                groups[3] = "00"
                
            groups[0] = f"{int(groups[0]):02d}"
            groups[3] = f"{int(groups[3]):02d}"
                
            if groups[1] and groups[4]:
                return f"{groups[0]}{groups[1]} to {groups[3]}{groups[4]}"
            elif not groups[1] and not groups[4]:
                return f"{groups[0]}:00 to {groups[3]}:00"
            else:
                raise ValueError
            
        else:
            raise ValueError
    else:
        raise ValueError

if __name__ == "__main__":
    main()
