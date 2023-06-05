import emoji

def main():
    emo = input("Input: ")
    print(emoji.emojize(f"Output: {emo} "))

if __name__ == "__main__":
    main()