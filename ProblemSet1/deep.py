def main():
    ans()

def ans():
    answer = input('What is the Answer to the Great Question of Life, the Universe and Everything?\n')
    key = "forty two"
    key2 = "forty-two"
    if answer.lower() == key2.lower():
        print('Yes')
    elif answer.lower() == key.lower():
        print('Yes')
    elif str(42) in answer :
        print('Yes')
    else:
        print('No')

main()
