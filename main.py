print("booting 'sol-os'", end="\r")
import time as t
t.sleep(1)
while True:
    print("(1)calc, (2)game2d, (3)operators, (4)github")
    from os import system, get_terminal_size
    clear = lambda : system("clear")
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
        rown -= 1
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
                clear()
                break
    elif i == "3":
        print("(0)not, (1)and (2)or")
        i = input()
        clear()
        o = None
        if i == "0":
            n = int(input("byte(0,1):"))
            o = not n
        elif i == "1":
            n1 = int(input("byte1(0,1):"))
            n2 = int(input("byte2(0,1):"))
            o = n1 and n2
        elif i == "2":
            n1 = int(input("byte1(0,1):"))
            n2 = int(input("byte2(0,1):"))
            o = n1 or n2       
        print(o)    
        t.sleep(1)           
    elif i == "4":
        print("https://github.com/Kolya142/sol-os")
        t.sleep(1)