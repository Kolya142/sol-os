print("booting 'sol-os'", end="\r")
import time as t
t.sleep(1)
while True:
    print("                ")
    print("(1)calc, (2)game2d", end="\r")
    from os import system, get_terminal_size
    clear = lambda : system("cls | clear")
    i = input()
    clear()
    if i == "1":
        n1 = int(input("n1:"))
        n2 = int(input("n2:"))
        w = input("?")
        clear()
        out = None
        if w == "+":
            out = n1 + n2
        elif w == "-":
            out = n1 - n2
        elif w == "sqrt":
            out = (n1)**0.5
        elif w == "/":
            out = n1 / n2
        elif w == "*":
            out = n1 * n2
        elif w == "**":
            out = n1 ** n2
        print(out, end="\r")
        t.sleep(1)
    elif i == "2":
        n = 0
        cols, rown = get_terminal_size()
        while True:
            clear()
            o = ""
            for i in range(cols * rown):
                if i == n:
                    o += "p"
                else:
                    o += "."
            print(o)
            i = input(":")
            if i == "w":
                n -= cols
            elif i == "a":
                n -= 1
            elif i == "s":
                n += cols
            elif i == "d":
                n += 1
            else:
                break