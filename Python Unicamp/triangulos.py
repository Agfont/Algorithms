# -*- coding: utf-8 -*-
l1 = float(input())
l2 = float(input())
l3 = float(input())

if l1 == l2 == l3 :
    print("Triângulo equilátero.")
    print("Triângulo acutângulo.")

elif l1 != l2 and l2 != l3 and l3 != l1 :
    if l1 > l2 and l1 > l3 :
        if l1 < l2 + l3 :
            if l1**2 < l2**2 + l3**2 :
                print("Triângulo escaleno.")
                print("Triângulo acutângulo.")
            elif l1**2 == l2**2 + l3**2 :
                print("Triângulo escaleno.")
                print("Triângulo retângulo.")
            elif l1**2 > l2**2 + l3**2 :
                print("Triângulo escaleno.")
                print("Triângulo obtusângulo.")
        else :
            print("Valores inválidos na entrada.")

    elif l2 > l1 and l2 > l3 :
        if l2 < l1 + l3 :
            if l2**2 < l1**2 + l3**2 :
                print("Triângulo escaleno.")
                print("Triângulo acutângulo.")
            elif l2**2 == l1**2 + l3**2 :
                print("Triângulo escaleno.")
                print("Triângulo retângulo.")
            elif l2**2 > l1**2 + l3**2 :
                print("Triângulo escaleno.")
                print("Triângulo obtusângulo.")
        else :
            print("Valores inválidos na entrada.")

    elif l3 > l1 and l3 > l2 :
        if l3 < l1 + l2 :
            if l3**2 < l2**2 + l1**2 :
                print("Triângulo escaleno.")
                print("Triângulo acutângulo.")
            elif l3**2 == l2**2 + l1**2 :
                print("Triângulo escaleno.")
                print("Triângulo retângulo.")
            elif l3**2 > l2**2 + l1**2 :
                print("Triângulo escaleno.")
                print("Triângulo obtusângulo.")
        else :
            print("Valores inválidos na entrada.")

else :
    print("Triângulo isósceles.")
    if l1**2 < l2**2 + l3**2 :
        print("Triângulo acutângulo.")
    elif l1**2 == l2**2 + l3**2 :
        print("Triângulo retângulo.")
    elif l1**2 > l2**2 + l3**2 :
        print("Triângulo obtusângulo.")
