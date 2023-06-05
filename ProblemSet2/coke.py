def main():
    print("Amount Due:" + str(50))
    c = int(input("Insert coin:"))
    insertcoin(c)

def insertcoin(b):
    # while loop to check if it is a valid coin
    while b not in (25, 10, 5):
        print("Amount Due:" + str(50))
        b = int(input("Insert coin:"))
    # while loop to get the amount due left
    a = 50
    while a > 0:
        a = a - b
        if a > 0:
            print("Amount Due:" + str(a))
            b = int(input("Insert Coin:"))
        else:
            a = abs(a)
            print("Change Owed: " + str(a))
            return# break

main()
