def main():
    greet = input("Greeting: ").lower().strip()
    print(f"${value(greet)}")




def value(greet):
    if greet.lower().startswith("hello"):
        return 0
    elif greet.lower().startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()