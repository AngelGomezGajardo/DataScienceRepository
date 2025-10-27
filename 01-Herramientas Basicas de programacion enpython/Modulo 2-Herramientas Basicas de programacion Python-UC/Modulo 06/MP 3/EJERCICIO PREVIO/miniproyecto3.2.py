#variables
ciclo=1
EstadoAtencion="pendiente"
LstExam=list()
Exam=dict()
Pacientes=dict()

#abre documentos
DocPacientes = open("pacientes.csv", "r")
DocExamenes=open("disponibilidad.txt","r")

for lineas in DocExamenes:
    limpia=lineas.strip()
    datos = limpia.split()
    clave = datos[0]
    valor = int(datos[1])
    Exam[clave] = valor
DocExamenes.close()

for lineas in DocPacientes:
    limpia = lineas.strip()
    datos = limpia.split(',')
    nombre = datos[0]
    examenes = datos[1:]
    Pacientes[nombre] = examenes
DocPacientes.close()

#extra la primera palabra
def ExtraePrimeraPalabra(menu):
    CleanM = menu.lstrip()
    CleanM = menu.split()
    return CleanM[0], CleanM[1]

#evalua si puede o no ser atendido y descuenta el valor del diccionario
def evaluaAtencion(nombre):
    resultado = ["rechazado", ""]
    if nombre not in Pacientes:
        return resultado
    for ex in Pacientes[nombre]:
        if ex not in Exam:
            resultado[1] = ex
            return resultado
        if Exam[ex] == 0:
            resultado[1] = ex
            return resultado
    for ex in Pacientes[nombre]:
        Exam[ex] = Exam[ex] - 1
    resultado[0] = "atendido"
    return resultado

#loop principal
while ciclo > 0:
    print("\nDisponibilidad actual:")
    for ex in Exam:
        print(ex, ":", Exam[ex])

    Menu = input("Bienvenido, ingrese la instruccion a continuación:\n")
    Instruccion, Nombre = ExtraePrimeraPalabra(Menu)

    if Instruccion == 'atender':
        resultado = evaluaAtencion(Nombre)
        EstadoAtencion = resultado[0]
        NProcedimiento = resultado[1]
        if EstadoAtencion == "atendido":
            print(f"se ha atendido a \"{Nombre}\" con éxito")
        else:
            print(f"no es posible atender a \"{Nombre}\", porque no existen horas para \"{NProcedimiento}\"")

    elif Instruccion == 'agregar':
        partes = Menu.split()
        for ex in partes[1:]:
            if ex in Exam:
                Exam[ex] = Exam[ex] + 1
            else:
                Exam[ex] = 1
        print("se han agregado correctamente las instrucciones")

    elif Instruccion == 'stop':
        print("se ha presionado \"stop\", el programa se detuvo. ¡Hasta pronto!")
        break
