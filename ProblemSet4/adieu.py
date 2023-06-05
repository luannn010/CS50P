import inflect

p = inflect.engine()

def main():
    name_list = []
    try:
        while True:
            name = input("Name: ")
            name_list.append(name)
    except EOFError:
        pass

    namelist = p.join(name_list)
    print(f"Adieu, adieu, to {namelist}")

if __name__ == "__main__":
    main()
