matrix = int(input("Enter Matrix Size: "))
dict = {}

for x in range(0, matrix):
    dict[x] = input(f"Shopping Item {x+1}: ")

print(f"You have {len(dict)} items in your cart")

while True:
    key = input("\nWhat would you like to do [C]hange items [R]emove [D]isplay  S[earch] ? ")

    if key == "*":
        print("Bye")
        break

    elif key == "S" or key == "s":
        search = input("Enter key (number) or item name to search: ")
        found = False

        if search.isdigit():  
            search = int(search)
            if search in dict:
                print(f"Found: key {search} contains '{dict[search]}'")
                found = True
        else:
            for k, v in dict.items():
                if v.lower() == search.lower():
                    print(f"Found '{v}' at key {k}")
                    found = True
                    break

        if not found:
            print(f"I'm sorry, {search} not in the cart.")

    elif key == "R" or key == "r":
        remove = input("Enter key (number) or item name to remove: ")
        removed = False

        if remove.isdigit():
            remove = int(remove)
            if remove in dict:
                print(f"The key {remove} with value '{dict[remove]}' has been deleted.")
                del dict[remove]
                removed = True
        else:
            for k, v in list(dict.items()):
                if v.lower() == remove.lower():
                    print(f"The key {k} with value '{v}' has been deleted.")
                    del dict[k]
                    removed = True
                    break

        if not removed:
            print(f"I'm sorry, {remove} not in the cart.")

    elif key == "D" or key == "d":
        print("KEY - VALUE")
        for x, y in dict.items():
            print(f"{x} - {y}")

    elif key == "C" or key == "c":
        change = input("Enter key (number) to change: ")
        if change.isdigit():
            change = int(change)
            if change in dict:
                print(f"Found item '{dict[change]}' at key {change}")
                dict[change] = input("Enter new value: ")
            else:
                print("Key not found in the cart.")
        else:
            print("Invalid input, must be a number.")

    else:
        print("Command not found")
