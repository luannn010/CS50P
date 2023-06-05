def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha():
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    i = 0
    while i < len(s)-1:
        if s[i].isalpha() and s[i+1] == "0":
            return False
        i += 1

    j = 1
    while j < len(s):
        if s[j-1].isdigit() and s[j].isalpha():
            return False
        j += 1


    if not s.isalnum():
        return False

    return True

if __name__ == "__main__":
    main()
