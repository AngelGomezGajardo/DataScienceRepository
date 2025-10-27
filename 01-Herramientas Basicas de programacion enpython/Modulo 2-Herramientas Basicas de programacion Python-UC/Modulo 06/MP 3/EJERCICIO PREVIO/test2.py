#extra la primera palabra
def ExtraePrimeraPalabra(menu):
    CleanM=menu.lstrip()
    CleanM=menu.split()
    #print(limpia[0])
    tamaño=len(CleanM)
    if tamaño>1:
        return CleanM[0], CleanM[1]
    if tamaño ==1:
        return CleanM[0],""
ciclo=1

while ciclo>0:
    Menu = (input("Bienvenido, ingrese la instruccion a continuación:\n"))

    Instruccion,Nombre=ExtraePrimeraPalabra(Menu)
    if Instruccion == 'atender':
        RevExam=True

        if RevExam==True:
            print(f"se a atendido a \"{Nombre}\" con exito")

        else:
            print(f"no es posible atender a \"{Nombre}\", porque no existen horas para \"{NProcedimiento}\"")

    elif Instruccion == 'agregar':
        print(f"se han agregado correctamente las instrucciones")

    elif Instruccion == 'stop':
        print("se a presionado \"stop\" el programa se detuvo, hasta pronto!")
        break
