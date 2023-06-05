import random

def main():
    level = get_level()

    score = 0
    i = 0
    while i < 10:
        X, Y = generate_integer(level)
        answer = input(f"{X} + {Y} = ")
        result = X + Y
        k = 0
        while k < 2:
            if answer != str(result):
                print("EEE")
                answer = input(f"{X} + {Y} = ")
                if answer != str(result):

                    k += 1
                else:
                    i += 1
                    break
            else:
                score += 1
                i += 1
                break
        else:
            i += 1

            print(f"{X} + {Y} = {X + Y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not 0 < level < 4:
                raise ValueError
        except ValueError:
            continue
        except EOFError:
            break
        return level


def generate_integer(level):
    if level == 1 :
        min_value = 0
    else:
        min_value = pow(10,(level - 1))

    max_value = pow(10,level) -1
    X = random.randint(min_value, max_value)
    Y = random.randint(min_value, max_value)
    return X, Y


if __name__ == "__main__":
    main()
