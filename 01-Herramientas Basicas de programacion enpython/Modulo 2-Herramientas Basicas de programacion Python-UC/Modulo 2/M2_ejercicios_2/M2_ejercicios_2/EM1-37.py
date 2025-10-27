import random
numero_aleatorio = random.randint(1,5)
nombre_persona = input("Ingresa tu nombre para poder asignarte a un grupo.")

if numero_aleatorio == 1:
    print(nombre_persona + " fuiste asignado/a al grupo ALERCE\n")
elif numero_aleatorio == 2:
    print(nombre_persona + " fuiste asignado/a al grupo BOLDO\n")
elif numero_aleatorio == 3:
    print(nombre_persona + " fuiste asignado/a al grupo CEREZO\n")
elif numero_aleatorio == 4:
    print(nombre_persona + " fuiste asignado/a al grupo DAMASCO\n")
elif numero_aleatorio == 5:
    print(nombre_persona + " fuiste asignado/a al grupo EUCALIPTUS\n")