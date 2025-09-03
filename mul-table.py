while True:
    row = int(input("Enter Row: "))
    col = int(input("Enter Column: "))

    if row < 0 or col < 0:
        print("Stopped")
        break
    search = int(input("Search Number: "))

    for x in range(1, row+1):
        for y in range(1, col+1):
            p = x*y
            if search==p:
                print(f"[{p}]", end=" ")
            else:
                print(f"{p}", end=" ")
        print("")