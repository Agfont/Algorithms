''' Exercício Básico
    Exemplo entrada: 1 + 1 '''
str1 = input()
if str1.isdigit() :
    op1 = int(str1)
    tipo_op1 = "int"
else :
    op1 = float(str1)
    tipo_op1 = "float"

operador = input()

str2 = input()
if str2.isdigit() :
    op2 = int(str2)
    tipo_op2 = "int"
else :
    op2 = float(str2)
    tipo_op2 = "float"

if operador == "+" :
    res = op1 + op2
    if tipo_op1 == "int" :
        if tipo_op2 == "int" :
            print(res)
        else :
            print(format(res,".2f"))
    elif tipo_op1 == "float" :
        print(format(res,".2f"))

elif operador == "-" :
    res = op1 - op2
    if tipo_op1 == "int" :
        if tipo_op2 == "int" :
            print(res)
        else :
            print(format(res,".2f"))
    elif tipo_op1 == "float" :
        print(format(res,".2f"))

elif operador == "*" :
    res = op1 * op2
    if tipo_op1 == "int" :
        if tipo_op2 == "int" :
            print(res)
        else :
            print(format(res,".2f"))
    elif tipo_op1 == "float" :
        print(format(res,".2f"))

elif operador == "//" :
    if tipo_op1 == "int" :
        if tipo_op2 == "int" :
            if op2 == int(0) :
                print("Erro.")
            else :
                res = op1 // op2
                print(res)
        else :
            if op2 == float(0.0) :
                print("Erro.")
            else :
                res = op1 // op2
                print(format(res,".2f"))
    elif tipo_op1 == "float" :
        if op2 == int(0) :
            print("Erro.")
        else :
            res = op1 // op2
            print(format(res,".2f"))

elif operador == "%" :
    if tipo_op1 == "int" :
        if tipo_op2 == "int" :
            if op2 == int(0) :
                print("Erro.")
            else :
                res = op1 % op2
                print(res)
        else :
            if op2 == float(0.0) :
                print("Erro.")
            else :
                res = op1 % op2
                print(format(res,".2f"))
    elif tipo_op1 == "float" :
        if op2 == int(0) :
            print("Erro.")
        else :
            res = op1 % op2
            print(format(res,".2f"))

elif operador == "/" :
    if op2 == int(0) :
        print("Erro.")
    elif op2 == float(0.0) :
        print("Erro.")
    else :
        res = op1 / op2
        print(format(res,".2f"))

elif operador == "**" :
    res = op1 ** op2
    if tipo_op1 == "int" :
        if tipo_op2 == "int" :
            print(res)
        else :
            print(format(res,".2f"))
    elif tipo_op1 == "float" :
        print(format(res,".2f"))
