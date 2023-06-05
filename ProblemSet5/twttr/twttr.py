def main():
    message = input('Input:')
    print("Output: " + shorten(message))


   
def shorten(word):
    vowels = "aeiouAEIOU"
    new_output = ""
    for a in word:
        if a not in vowels:
            new_output += a
    return new_output



if __name__ == "__main__":
    main()

