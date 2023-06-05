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
    date = input("Date: ")
    if "," in date:
        month_day, year = date.split(",")
        year = year.strip()
        month, day = map(str.strip, month_day.split())
        month = months.index(month) + 1
        if 1 <= month <= 12 and 1 <= int(day) <= 31 and len(str(year)) == 4:
            return f"{year}-{month:02}-{int(day):02}"
    elif "/" in date:
        month, day, year = map(int, date.split("/"))
        if 1 <= month <= 12 and 1 <= day <= 31 and len(str(year)) == 4:
            return f"{year}-{month:02}-{day:02}"
    raise ValueError

try:
    result = main()
    print(result)
except ValueError:
    main()
