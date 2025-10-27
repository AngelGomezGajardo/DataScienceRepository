from numpy.ma.core import append

laLista=list()

f = open("amigos.txt", "r")
for lineas in f:
    limpia=lineas.strip()
    datos=lineas.split()
    laLista.append(datos)
print(laLista[0])

