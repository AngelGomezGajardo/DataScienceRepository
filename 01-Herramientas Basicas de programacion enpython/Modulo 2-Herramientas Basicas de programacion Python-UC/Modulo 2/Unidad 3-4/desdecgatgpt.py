# Variables de despacho
Cerca = 1000
Normal = 5000
Lejos = 10000

#########################################################################
# Función modificada por ti para obtener identificador de tienda
def NombreTiendas(var1):
    X = var1.upper()
    PtresLetras = X[0:3]
    return PtresLetras
#########################################################################
# Función modificada por ti para comparar identificadores
def compara(x, y):
    str2 = "2"
    if x == y:
        y = y + str2
    return y
#########################################################################

# Calcula el total para una instrucción
def CalcXtienda(dcto, dspcho, ctdd, prc):
    descuento = int(dcto)
    despacho = int(dspcho)
    cantidad = int(ctdd)
    precio = int(prc)
    if cantidad >= 10:
        total = -descuento + despacho + ((cantidad - 1) * precio)
    else:
        total = -descuento + despacho + (cantidad * precio)

    if total < 0:
        total = 0

    return total


# Procesa el texto ingresado por el usuario
def separa(instr):
    descuento = 0
    despacho = 0
    unidades = 0
    precio = 0

    partes = instr.lower().split()

    if partes[0] == "descuento":
        descuento = partes[1]
    elif partes[0] == "despacho":
        categoria = partes[1].lower()
        if categoria == "cerca":
            despacho = Cerca
        elif categoria == "normal":
            despacho = Normal
        elif categoria == "lejos":
            despacho = Lejos
    else:
        unidades = partes[0]
        precio = partes[1]

    return descuento, despacho, unidades, precio


# INICIO DEL PROGRAMA
TotalT = [0, 0]

NombreT1 = input("Ingrese el nombre de la tienda 1: ")
NombreT2 = input("Ingrese el nombre de la tienda 2: ")

nt1 = NombreTiendas(NombreT1)
nt2 = NombreTiendas(NombreT2)
nt2 = compara(nt1, nt2)

nombres = [nt1, nt2]

print(nt1, "$" + str(TotalT[0]))
print(nt2, "$" + str(TotalT[1]))

# Ciclo de rondas
while TotalT[0] <= 100000 and TotalT[1] <= 100000:
    for j in range(2):  # j = 0 para tienda 1, j = 1 para tienda 2
        print("\nIngrese instrucciones para tienda", j + 1)

        inst1 = input()
        desc, desp, unid, pre = separa(inst1)
        costo1 = CalcXtienda(desc, desp, unid, pre)

        inst2 = input()
        desc, desp, unid, pre = separa(inst2)
        costo2 = CalcXtienda(desc, desp, unid, pre)

        inst3 = input()
        desc, desp, unid, pre = separa(inst3)
        costo3 = CalcXtienda(desc, desp, unid, pre)

        total_ronda = costo1 + costo2 + costo3

        TotalT[j] = TotalT[j] + total_ronda
        print(nombres[j], "$" + str(TotalT[j]))

    if TotalT[0] > 100000 or TotalT[1] > 100000:
        break

# Resultado final
print("\n--- Resultado final ---")
print(nombres[0], ":", "$" + str(TotalT[0]))
print(nombres[1], ":", "$" + str(TotalT[1]))

if TotalT[0] > 100000 and TotalT[1] > 100000:
    print("Empate.")
elif TotalT[0] > 100000:
    print(NombreT2, "es mejor.")
else:
    print(NombreT1, "es mejor.")
