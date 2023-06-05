def main():
    message = input('Input:')
    print("Output: " + shorten(message))
def shorten(k):
    vowels = "aeiouAEIOU"
    new_output = ""
    for a in k:
        if a not in vowels:
            new_output += a
    return new_output

main()

