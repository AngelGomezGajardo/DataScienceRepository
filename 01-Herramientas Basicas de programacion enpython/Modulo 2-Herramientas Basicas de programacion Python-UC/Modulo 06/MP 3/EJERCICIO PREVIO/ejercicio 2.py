
laLista=list()

f = open("ramos.csv", "r")
for lineas in f:
    limpia=lineas.strip()
    datos=lineas.split()
    laLista.append(datos)
print(laLista)