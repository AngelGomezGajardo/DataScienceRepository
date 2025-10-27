from logging.config import dictConfig

from numba.experimental.jitclass.overloads import class_instance_overload

laLista=list()
Diccionario={}
f = open("ramos2.csv", "r")
for lineas in f:
    limpia=lineas.strip()
    datos=lineas.split(',')
    laLista.append(datos)

    Clave=datos[0]
    valor=datos[1],datos[2],datos[3]
    Diccionario[Clave]=valor
print(f"el valor para 1234567 {Diccionario['1234567']}")
