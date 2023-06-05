import random

def main():
    while True:
        level = input("Level: ")
        if not level.isdigit():
            continue
        if int(level) < 1:
            continue
        number = random.randint(1, int(level))

        try:
            while True:
                try:
                    guess = int(input("Guess: "))
                except ValueError:
                    continue

                if guess > number:
                    print("Too large!")
                elif guess < number:
                    print("Too small!")
                elif guess == number:
                    print("Just right!")
                    raise EOFError

        except EOFError:
            break

if __name__ == "__main__":
    main()
