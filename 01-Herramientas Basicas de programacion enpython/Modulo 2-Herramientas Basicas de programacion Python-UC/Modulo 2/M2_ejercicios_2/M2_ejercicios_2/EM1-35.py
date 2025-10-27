import random
numero_aleatorio = random.randint(1,3)
nombre_persona = input("Ingresa tu nombre para poder asignarte a un grupo.")

if numero_aleatorio == 1:
    print(nombre_persona + " fuiste asignado/a al grupo ALERCE\n")
else:
    if numero_aleatorio == 2:
        print(nombre_persona + " fuiste asignado/a al grupo BOLDO\n")
    else:
        print(nombre_persona + " fuiste asignado/a al grupo CEREZO\n")