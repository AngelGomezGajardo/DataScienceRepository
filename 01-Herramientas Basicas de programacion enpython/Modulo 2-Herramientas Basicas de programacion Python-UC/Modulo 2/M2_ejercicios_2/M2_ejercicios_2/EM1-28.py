numero = int(input("Ingrese el número que desea comprobar que sea menor que 3 o mayor que 10\n"))
menor_que_3 = numero < 3
mayor_que_10 = numero > 10
print(menor_que_3 or mayor_que_10)