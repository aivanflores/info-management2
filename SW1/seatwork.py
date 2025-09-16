def rupee(dollar):
    return dollar * 88.17

def pound(dollar):
    return dollar * 0.73

def yen(dollar):
    return dollar * 7.12

display = []
while True:
    dollar = input("Enter Dollar($)(* to exit): ")
    if dollar == "*":
        print("Bye!")
        break

    set = dollar.split('@')

    for num in set:
        num = int(num)  
        r = rupee(num)
        p = pound(num)
        y = yen(num)
        display.append((num, r, p, y))

    print("Dollar ($) Indian Ruppe (R)  British (Pound)  China (Y)")
    for d, r1, p1, y1 in display:
         print(f"{d:<11}{r1:<18.2f}{p1:<18.2f}{y1:<.2f}")
