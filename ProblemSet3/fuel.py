


def main():
    frac = input("Fraction: ")
    parts = frac.split("/")
    x = int(parts[0])
    y = int(parts[1])
    div = x / y * 100

    if div <= 1:
        print("E")
    elif 99 <= div <= 100 :
        print("F")
    elif x / y > 1:
        raise ValueError
    else:
        print(str(round(div)) + "%")

try:
    main()
except ValueError:
    main()
except ZeroDivisionError:
    main()



