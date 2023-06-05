def main():
    camelcase = input('camelCase:')
    print("snake_case:" + cameltosnake(camelcase))


def cameltosnake(string):
    snake= ""
    for char in string:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

main()
