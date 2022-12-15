def main():
    greeting()
def greeting():
    greet = input("Greeting: ")
    if 'hello' in greet.lower():
        print('$0')
    elif greet.strip().lower().startswith('h'):
        print('$20')
    else:
        print('$100')
    return
main()
