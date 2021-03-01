N = int(input())
if N < 1 or N > 100:
  print("Valor inválido na entrada.")

else:
  dic = {}
  dic["a"] = []
  dic["v"] = []
  dic["d"] = []
  nomes = []
  la = []
  for j in range(N):
    assassino, vitima, detetive = input().split()
    dic["a"].append(assassino)
    dic["v"].append(vitima)
    dic["d"].append(detetive)
    la.append(assassino)
    if assassino not in nomes:
      nomes.append(assassino)
    if vitima not in nomes:
      nomes.append(vitima)
    if detetive not in nomes:
      nomes.append(detetive)
  nomes = sorted(nomes)
  print(60 * "-")

  for k in range(len(nomes)):
    mv = 0
    md = 0
    ma = 0
    if nomes[k] in dic["d"]:
      if nomes[k] in dic["v"]:
        print(nomes[k], "(in memoriam): detetive.")
      else:
        print(nomes[k]+": detetive.")
      cr = dic["d"].count(nomes[k])
      print("  Resolveu" ,cr, "caso(s).")
      if nomes[k] in dic["a"]:
        mt = dic["a"].count(nomes[k])
        for m in range (mt):
          vref = la.index(nomes[k])
          if dic["v"][vref] in dic["d"]:
            md += 1
          elif dic["v"][vref] in dic["a"]:
            ma += 1
          elif dic["v"][vref] in dic["v"]:
            mv += 1
          la.insert(vref, "0")
          la.remove(nomes[k])

        if md:
          print("  Matou" ,md, "detetive(s).")
        if ma:
          print("  Matou" ,ma, "assassino(s).")
        if mv:
          print("  Matou" ,mv, "inocente(s).")
      print(60 * "-")

    elif nomes[k] in dic["a"]:
      if nomes[k] in dic["v"]:
        print(nomes[k], "(in memoriam): assassino(a).")
      else:
        print(nomes[k]+": assassino(a).")
      if nomes[k] in dic["a"]:
        mt = dic["a"].count(nomes[k])
        for m in range (mt):
          vref = la.index(nomes[k])
          if dic["v"][vref] in dic["d"]:
            md += 1
          elif dic["v"][vref] in dic["a"]:
            ma += 1
          elif dic["v"][vref] in dic["v"]:
            mv += 1
          la.insert(vref, "0")
          la.remove(nomes[k])

        if md:
          print("  Matou" ,md, "detetive(s).")
        if ma:
          print("  Matou" ,ma, "assassino(s).")
        if mv:
          print("  Matou" ,mv, "inocente(s).")
      print(60 * "-")

    elif nomes[k] in dic["v"]:
      print(nomes[k], "(in memoriam): vítima inocente.")
      print(60 * "-")
