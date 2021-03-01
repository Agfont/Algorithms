# -*- coding: utf-8 -*-
objeto = input()
base = int(input())
caractere = input()

if base >= 3 and (base+1)%2==0:
    if objeto == "TR":
        for i in range(1,base+1,2):
            print(caractere*i)
    elif objeto == "TRI":
        for i in range(base,0,-2):
            print(caractere*i)
    elif objeto == "TI":
        for i in range(1,base+1,2):
            if i < base:
                print(((base-i-1)//2)*" ", caractere*i)
            elif i == base:
                print(caractere*i)
    elif objeto == "TII":
        for i in range(base,0,-2):
            if i < base:
                print(((base-i-1)//2)*" ", caractere*i)
            elif i == base:
                print(caractere*i)
    elif objeto == "A":
        for i in range(base,0,-2):
            if i < base:
                print(((base-i-1)//2)*" ", caractere*i)
            elif i == base:
                print(caractere*i)
        for i in range(1,base+1,2):
            if i != 1:
                if i < base:
                    print(((base-i-1)//2)*" ", caractere*i)
                elif i == base:
                    print(caractere*i)
    elif objeto == "E":
        for i in range(1,base+1,2):
            if i < base:
                print((base+(base-i)//2-1)*" ", caractere*i)
            elif i == base:
                print(caractere*3*i)
        for i in range(base,0,-2):
            if i < base:
                print(((base-i-1)//2)*" ", caractere*i, (2*base-i-2)*" ", caractere*i)
        for i in range(1,base+1,2):
            if i != 1:
                if i < base:
                    print(((base-i-1)//2)*" ", caractere*i, (2*base-i-2)*" ", caractere*i)
                elif i == base:
                    print(caractere*3*i)
        for i in range(base,0,-2):
            if i < base:
                print((base+(base-i)//2-1)*" ", caractere*i)
    else:
        print("Objeto inválido.")
else :
    print("Base inválida.")
