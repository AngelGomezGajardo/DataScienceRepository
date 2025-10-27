import random
numero_dado=random.randint(1,6)
print("El número que arrojó el dado fue: "+str(numero_dado)+"\n")

if numero_dado%2==0:
    print("Este es un número par. \n")
else:
    print("Este es un número impar. \n")