diagrama_entrada = []
altura = 0
palavras = []
while 0 < 1:
    l = input()
    if l.isdigit():
        n = int(l)
        break
    else:
        l = l.split()
        diagrama_entrada.append(l)
        altura += 1
largura = len(diagrama_entrada[0])
diagrama_saida = [["." for x in range(largura)] for y in range(altura)]
for a in range(n):
    p = input()
    palavras.append(p)

print(diagrama_entrada)
print("Palavras:", palavras)

for b in range(len(palavras)):
    count = 0
    for d in range(altura):
        quant = diagrama_entrada[d].count(palavras[b][0])
        for j in range(quant):
            if palavras[b][0] in diagrama_entrada[d]:
                posição = diagrama_entrada[d].index(palavras[b][0])
                if palavras[b][1] in diagrama_entrada[d]:
                    if diagrama_entrada[d][posição+1] == palavras[b][1]:
                        count = 2
                        pass
                        for c in range(len(palavras[b])-2):
                            if diagrama_entrada[d][posição+2+c] == palavras[b][c+2]:
                                count += 1

                    elif diagrama_entrada[d][posição-1] == palavras[b][1]:
                        count = 2
                        pass
                        for c in range(len(palavras[b])-2):
                            if diagrama_entrada[d][posição-2-c] == palavras[b][c+2]:
                                count += 1


                if palavras[b][1] in diagrama_entrada[d-1]:
                    if diagrama_entrada[d-1][posição] == palavras[b][1]:
                        count = 2
                        pass
                        for c in range(len(palavras[b])-2):
                            if diagrama_entrada[d-2-c][posição] == palavras[b][c+2]:
                                count += 1

                    elif diagrama_entrada[d-1][posição+1] == palavras[b][1]:
                        count = 2
                        pass
                        for c in range(len(palavras[b])-2):
                            if diagrama_entrada[d-2-c][posição+2+c] == palavras[b][c+2]:
                                count += 1

                    elif diagrama_entrada[d-1][posição-1] == palavras[b][1]:
                        count = 2
                        pass
                        for c in range(len(palavras[b])-2):
                            if diagrama_entrada[d-2-c][posição-2-c] == palavras[b][c+2]:
                                count += 1


                if palavras[b][1] in diagrama_entrada[d+1]:
                    if diagrama_entrada[d+1][posição] == palavras[b][1]:
                        count = 2
                        pass
                        for c in range(len(palavras[b])-2):
                            if diagrama_entrada[d+2+c][posição] == palavras[b][c+2]:
                                count += 1

                    elif diagrama_entrada[d+1][posição+1] == palavras[b][1]:
                        count = 2
                        pass
                        for c in range(len(palavras[b])-2):
                            if diagrama_entrada[d+2+c][posição+2+c] == palavras[b][c+2]:
                                count += 1

                    elif diagrama_entrada[d+1][posição-1] == palavras[b][1]:
                        count = 2
                        pass
                        for c in range(len(palavras[b])-2):
                            if diagrama_entrada[d+2+c][posição-2-c] == palavras[b][c+2]:
                                count += 1

    if count == len(palavras[b]):
        print(count)
