#list months like words
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    
    #input
    date = input("Date: ").strip()
    
    #replace / in case is all digit
    try_date = date.replace("/", "")
    
    #check if is all digit or not
    try:
        if try_date.isdigit():
            date = date.split("/")
            month, day, year = date
            month, day, year = int(month), int(day), int(year)
        else:
            if "," in date:
                date = date.replace(",", "")
                date = date.split(" ")
                month, day, year = date
                month = months.index(month) + 1
                month, day, year = int(month), int(day), int(year)
            else:
                main()
    except ValueError:
        main()
    else:
        #loop in case user not put the right input
        while True:
            if 0 < month < 13 and 0 < day < 32:
                order(month, day, year)
                break
            else: 
                main()
        
#defination of the other function
def order(month, day, year):
    print(f"{year:04}-{month:02}-{day:02}")
        
main()