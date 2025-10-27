#datos
from win32comext.directsound.directsound import DSCAPS
from win32con import DCTT_BITMAP

Cerca=1000
Normal=5000
Lejos=10000
Rs1=0
Rs2=0

def NombreTiendas(var1):
    X=var1.upper()
    PtresLetras=X[0:3]
    return PtresLetras
def compara(x,y):
    str2 = "2"
    if x == y:
        y=y+str2
    return y


def CalcXtienda(Dcto,Dspch,X,Z):
    if X>10:
        VU=Z/X
        Resultado = -Dcto + Dspch + ((X-1) * Z)
        return Resultado
    else:
        Resultado=-Dcto+Dspch+(X*Z)
    return Resultado

#xz=input("primer segunda: ")
#palabra=xz.split(" ")
#print(palabra[0])
#print(palabra[1])

costo1=CalcXtienda(0,0,12,1000)
print(costo1)
#NT1=input("ingrese la tienda 1: ")
#NT2=input("ingrese la tienda 2: ")
#NT1=NombreTiendas(NT1)
#NT2=NombreTiendas(NT2)
#NT2=compara(NT1, NT2)


#print("nombre de la tienda 1", NT1)
#print("nombre de la tienda 2", NT2)