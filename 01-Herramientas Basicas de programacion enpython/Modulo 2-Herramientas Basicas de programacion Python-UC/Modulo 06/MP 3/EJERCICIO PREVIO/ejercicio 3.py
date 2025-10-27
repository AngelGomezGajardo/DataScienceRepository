
dicccionario = {}
lista=[['Python','3'], ['R','1'], ['Elixir','4']]

clave = lista[0][0]
param = lista[0][1]


for par in lista:
    clave = par[0]
    valor = int(par[1])
    print(clave, valor)
    dicccionario[clave] = valor