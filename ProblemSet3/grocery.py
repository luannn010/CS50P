def main():
    list = []
    unique = []
    while True:

        try:
            grocery = input()
            list.append(grocery.upper())

        except EOFError:

            for grocery in list:
                if grocery not in unique:
                    unique.append(grocery)
            unique.sort()
            GroceryList = {}
            for grocery in unique:
                GroceryList[grocery] = list.count(grocery)
            for x,y in GroceryList.items():
                print(f"{y} {x}")
            break


main()